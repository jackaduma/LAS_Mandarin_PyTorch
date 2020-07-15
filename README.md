# **LAS_Mandarin_PyTorch**

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/LAS_Mandarin_PyTorch)


This code is a PyTorch implementation for paper: [**Listen, Attend and Spell**](https://arxiv.org/abs/1508.01211]), a nice work on End-to-End **ASR**, **Speech Recognition** model.

also provides a **Chinese Mandarin ASR** pretrained model.

------

## **Listen-Attend-Spell**

### **Google Blog Page** 
[Improving End-to-End Models For Speech Recognition](https://ai.googleblog.com/2017/12/improving-end-to-end-models-for-speech.html)

The LAS architecture consists of 3 components. The listener encoder component, which is similar to a standard AM, takes the a time-frequency representation of the input speech signal, x, and uses a set of neural network layers to map the input to a higher-level feature representation, henc. The output of the encoder is passed to an attender, which uses henc to learn an alignment between input features x and predicted subword units {yn, … y0}, where each subword is typically a grapheme or wordpiece. Finally, the output of the attention module is passed to the speller (i.e., decoder), similar to an LM, that produces a probability distribution over a set of hypothesized words.


![Components of the LAS End-to-End Model.
](https://4.bp.blogspot.com/-D26UVY-JPh4/WjK9bo6LVtI/AAAAAAAACRk/ABz4VpV0uvUywryKqaaIXgFz4w-JukTegCLcBGAs/s640/image1.png "Components of the LAS End-to-End Model.
")

Components of the LAS End-to-End Model.


------

**This repository contains:**

1. [model code](core) which implemented the paper.
2. [generate vocab file](generate_vocab_file.py), you can use to generate your vocab file for [your dataset](dataset).
3. [training scripts](train_asr.py) to train the model.
4. [testing scripts](test_asr.py) to test the model.

------

## **Table of Contents**

- [**LAS_Mandarin_PyTorch**](#las_mandarin_pytorch)
  - [**Listen-Attend-Spell**](#listen-attend-spell)
    - [**Google Blog Page**](#google-blog-page)
  - [**Table of Contents**](#table-of-contents)
  - [**Requirement**](#requirement)
  - [**Usage**](#usage)
    - [**preprocess**](#preprocess)
    - [**train**](#train)
    - [**test**](#test)
  - [**Pretrained**](#pretrained)
    - [**English**](#english)
    - [**Chinese Mandarin**](#chinese-mandarin)
  - [**Demo**](#demo)
  - [**TodoList**](#todolist)
  - [**License**](#license)


------


## **Requirement** 

```bash
pip install -r requirements.txt
```
## **Usage**

### **preprocess**

```python
python generate_vocab_file_aishell.py --input_file $DATA_DIR/data_aishell/transcript_v0.8.txt --output_file ./aishell_vocab.txt --mode character --vocab_size 5000
```

it will create a vocab file named **aishell_vocab.txt** in your folder.


### **train** 

Before training, you need to write your dataset code in package [dataset](dataset).

If you want use my aishell dataset code, you also should take care about the transcripts file path in [data/aishell.py](dataset/aishell.py) line 26:

```python
src_file = "/data/Speech/SLR33/data_aishell/" + "transcript/aishell_transcript_v0.8.txt"
```

When ready. 

Let's train:

```python
python main.py --config ./config/aishell
```

### **test**

```python
python main.py
```

------

## **Pretrained**

### **English**

### **Chinese Mandarin**

a pretrained model training on AISHELL-Dataset

download from [Google Drive](https://drive.google.com/file/d/1iamizL98NWIPw4pw0nF-7b6eoBJrxEfj/view?usp=sharing) <735MB>

------

## **Demo**

Samples:


[S0913(./data/S0913/BAC009S0913W0351.wav)](https://drive.google.com/file/d/14zU1mI8QtoBwb8cHkNdZiPmXI6Mj6pVW/view?usp=sharing)

[GaoXiaoSong(./data/gaoxiaosong/gaoxiaosong_1.wav)](https://drive.google.com/file/d/1s0ip6JwnWmYoWFcEQBwVIIdHJSqPThR3/view?usp=sharing)



[Converted from S0913 to GaoXiaoSong (./converted_sound/S0913/BAC009S0913W0351.wav)](https://drive.google.com/file/d/1S4vSNGM-T0RTo_aclxRgIPkUJ7NEqmjU/view?usp=sharing)

------
## **TodoList**

- [x] Dataset
  - [ ] [LibriSpeech]() for English Speech Recognition
  - [x] [AISHELL-Speech](https://openslr.org/33/) for Chinese Mandarin Speech Recognition
- [x] Usage
  - [x] Training
  - [x] Test
  - [x] Infer 
- [ ] Demo

------

## **License**

[MIT](LICENSE) © Kun