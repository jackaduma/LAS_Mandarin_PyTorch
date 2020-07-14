# **LAS_Mandarin_PyTorch**

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/LAS_Mandarin_PyTorch)

## **Listen, attend and spell Model**

This code is PyTorch implemented for [Listen, Attend and Spell](https://arxiv.org/abs/1508.01211])

------

## **LAS**

### [**Publication Page**](https://research.google/pubs/pub44926/)




![network](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc2/images/network.png "network")


------

**This repository contains:**

1. [model code](model_tf.py) which implemented the paper.
2. [audio preprocessing script](preprocess_training.py) you can use to create cache for [training data](data).
3. [training scripts](train.py) to train the model.
4. [Examples of Voice Conversion](converted_sound/) - converted result after training.

------

## **Table of Contents**

- [](#)
- [**LAS_Mandarin_PyTorch2**](#las_mandarin_pytorch2)
- [**LAS**](#las)
  - [**Publication Page**](#publication-page)
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

[Apache2.0](LICENSE) © Kun