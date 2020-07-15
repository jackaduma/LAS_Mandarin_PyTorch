#! python
# -*- coding: utf-8 -*-
# Author: kun
# @Time: 2019-10-30 14:40

import os
from tqdm import tqdm
from pathlib import Path
from os.path import join, getsize
from joblib import Parallel, delayed
from torch.utils.data import Dataset

# Additional (official) text core provided
OFFICIAL_TXT_SRC = ['librispeech-lm-norm.txt']
# Remove longest N sentence in librispeech-lm-norm.txt
REMOVE_TOP_N_TXT = 5000000
# Default num. of threads used for loading LibriSpeech
READ_FILE_THREADS = 1


def read_text(file):
    '''Get transcription of target wave file,
       it's somewhat redundant for accessing each txt multiplt times,
       but it works fine with multi-thread'''
    # print("read_text: file {}".format(file))
    src_file = "/opt/pa/datasets/Aishell/" + "transcript/aishell_transcript_v0.8.txt"
    idx = file.split('/')[-1].split('.')[0]

    with open(src_file, 'r') as fp:
        for line in fp:
            if idx == line.split(' ')[0]:
                line = line.strip('\n')
                aishell_word_list = line.split(' ')
                # print("aishell_word_list: ", aishell_word_list)
                new_list = []
                for word in aishell_word_list[1:]:  # 去除idx
                    if word != ' ' and word != '':
                        if len(word) == 1:
                            new_list.append(word)
                        else:
                            for char in word:
                                new_list.append(char)

                # print("new_list: ", new_list)
                new_line = ' '.join(new_list).strip(' ')
                # print("new_line: ", new_line)
                char_list = [c for c in new_line.split(' ')]
                # print("char_list: ", char_list)
                trans_text = "".join(char_list)
                return trans_text, file

    return None, file


class AishellDataset(Dataset):
    def __init__(self, path, split, tokenizer, bucket_size, ascending=False):
        # Setup
        print("[AishellDataset] path: {}, split: {}".format(path, split))
        self.path = path
        self.bucket_size = bucket_size

        # List all wave files
        file_list = []
        for s in split:
            split_path = Path(join(path, s))
            split_list = list(split_path.rglob("*.wav"))
            assert len(split_list) > 0, "No data found @ {}".format(path)
            print("AishellDataset {} found wav data: {}".format(s, len(split_list)))
            file_list += split_list

        # Read text
        text = Parallel(n_jobs=READ_FILE_THREADS)(
            delayed(read_text)(str(f)) for f in file_list)
        print("text len: {}".format(len(text)))
        # text = Parallel(n_jobs=-1)(delayed(tokenizer.encode)(txt) for txt in text)
        new_text = []
        new_file_list = []
        for t, f in text:
            if t is not None:
                new_text.append(t)
                new_file_list.append(f)
        print("remove None, then wav data: {}, text len: {}".format(len(new_file_list), len(new_text)))

        text = [tokenizer.encode(txt) for txt in new_text]

        # Sort dataset by text length
        # file_len = Parallel(n_jobs=READ_FILE_THREADS)(delayed(getsize)(f) for f in file_list)
        self.file_list, self.text = zip(*[(f_name, txt)
                                          for f_name, txt in sorted(zip(new_file_list, text), reverse=not ascending, key=lambda x: len(x[1]))])

    def __getitem__(self, index):
        # print("[AishellDataset  __getitem__] index: {}".format(index))
        if self.bucket_size > 1:
            # Return a bucket
            index = min(len(self.file_list) - self.bucket_size, index)
            return [(f_path, txt) for f_path, txt in
                    zip(self.file_list[index:index + self.bucket_size], self.text[index:index + self.bucket_size])]
        else:
            return self.file_list[index], self.text[index]

    def __len__(self):
        return len(self.file_list)


class AishellTextDataset(Dataset):
    def __init__(self, path, split, tokenizer, bucket_size):
        # Setup
        self.path = path
        self.bucket_size = bucket_size
        self.encode_on_fly = False
        read_txt_src = []

        # List all wave files
        file_list, all_sent = [], []

        for s in split:
            if s in OFFICIAL_TXT_SRC:
                self.encode_on_fly = True
                with open(join(path, s), 'r') as f:
                    all_sent += f.readlines()
            file_list += list(Path(join(path, s)).rglob("*.wav"))
        assert (len(file_list) > 0) or (len(all_sent) > 0), "No data found @ {}".format(path)

        # Read text
        text = Parallel(n_jobs=READ_FILE_THREADS)(
            delayed(read_text)(str(f)) for f in file_list)
        all_sent.extend(text)
        del text

        # Encode text
        if self.encode_on_fly:
            self.tokenizer = tokenizer
            self.text = all_sent
        else:
            self.text = [tokenizer.encode(txt) for txt in tqdm(all_sent)]
        del all_sent

        # Read file size and sort dataset by file size (Note: feature len. may be different)
        self.text = sorted(self.text, reverse=True, key=lambda x: len(x))
        if self.encode_on_fly:
            del self.text[:REMOVE_TOP_N_TXT]

    def __getitem__(self, index):
        if self.bucket_size > 1:
            index = min(len(self.text) - self.bucket_size, index)
            if self.encode_on_fly:
                for i in range(index, index + self.bucket_size):
                    if type(self.text[i]) is str:
                        self.text[i] = self.tokenizer.encode(self.text[i])
            # Return a bucket
            return self.text[index:index + self.bucket_size]
        else:
            if self.encode_on_fly and type(self.text[index]) is str:
                self.text[index] = self.tokenizer.encode(self.text[index])
            return self.text[index]

    def __len__(self):
        return len(self.text)
