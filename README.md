# **LAS_Mandarin_PyTorch**

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/LAS_Mandarin_PyTorch)

This code is PyTorch implemented for [**Listen, Attend and Spell**](https://arxiv.org/abs/1508.01211])

------

## **LAS**

### **Google Blog Page:** [Improving End-to-End Models For Speech Recognition](https://ai.googleblog.com/2017/12/improving-end-to-end-models-for-speech.html)

The LAS architecture consists of 3 components. The listener encoder component, which is similar to a standard AM, takes the a time-frequency representation of the input speech signal, x, and uses a set of neural network layers to map the input to a higher-level feature representation, henc. The output of the encoder is passed to an attender, which uses henc to learn an alignment between input features x and predicted subword units {yn, … y0}, where each subword is typically a grapheme or wordpiece. Finally, the output of the attention module is passed to the speller (i.e., decoder), similar to an LM, that produces a probability distribution over a set of hypothesized words.


![Components of the LAS End-to-End Model.
](https://4.bp.blogspot.com/-D26UVY-JPh4/WjK9bo6LVtI/AAAAAAAACRk/ABz4VpV0uvUywryKqaaIXgFz4w-JukTegCLcBGAs/s640/image1.png "Components of the LAS End-to-End Model.
")

Components of the LAS End-to-End Model.



------

**This repository contains:**

1. [model code](model_tf.py) which implemented the paper.
2. [audio preprocessing script](preprocess_training.py) you can use to create cache for [training data](data).
3. [training scripts](train.py) to train the model.
4. [Examples of Voice Conversion](converted_sound/) - converted result after training.

------

## **Table of Contents**

- [](#)
- [**LAS_Mandarin_PyTorch**](#las_mandarin_pytorch)
- [**LAS**](#las)
  - [**Google Blog Page**](#publication-page)
- [**Table of Contents**](#table-of-contents)
- [**Requirement**](#requirement)
- [**Usage**](#usage)
  - [**preprocess**](#preprocess)
  - [**train**](#train)
- [**Pretrained**](#pretrained)
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
python preprocess_training.py
```
is short for

```python
python preprocess_training.py --train_A_dir ./data/S0913/ --train_B_dir ./data/gaoxiaosong/ --cache_folder ./cache/
```


### **train** 
```python
python train.py
```

is short for

```python
python train.py --logf0s_normalization ./cache/logf0s_normalization.npz --mcep_normalization ./cache/mcep_normalization.npz --coded_sps_A_norm ./cache/coded_sps_A_norm.pickle --coded_sps_B_norm ./cache/coded_sps_B_norm.pickle --model_checkpoint ./model_checkpoint/ --resume_training_at ./model_checkpoint/_CycleGAN_CheckPoint --validation_A_dir ./data/S0913/ --output_A_dir ./converted_sound/S0913 --validation_B_dir ./data/gaoxiaosong/ --output_B_dir ./converted_sound/gaoxiaosong/
```

------

## **Pretrained**

a pretrained model which converted between S0913 and GaoXiaoSong

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
  - [ ] VC
  - [x] Chinese Male Speakers (S0913 from [AISHELL-Speech](https://openslr.org/33/) & [GaoXiaoSong: a Chinese star](https://en.wikipedia.org/wiki/Gao_Xiaosong))
- [x] Usage
  - [x] Training
  - [x] Example 
- [ ] Demo

------

## **License**

[MIT](LICENSE) © Kun