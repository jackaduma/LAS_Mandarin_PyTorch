# **LAS_Mandarin_PyTorch**

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/LAS_Mandarin_PyTorch)

[**中文说明**](./README.zh-CN.md) | [**English**](./README.md)

本项目使用PyTorch复现论文：[**Listen, Attend and Spell**](https://arxiv.org/abs/1508.01211]), 实现了一个端到端的**语音识别， ASR**的深度模型.

同时，也提供一个**中文普通话的语音识别 ASR** 的预训练模型.

- [x] 数据集
  - [ ] [LibriSpeech]() for English Speech Recognition
  - [x] [AISHELL-Speech](https://openslr.org/33/) for Chinese Mandarin Speech Recognition
- [x] 用法
  - [x] generate vocab file
  - [x] 训练
  - [x] 验证
  - [ ] 推理 
- [ ] Demo

------

## **Listen-Attend-Spell**

### **谷歌博客主页** 

[Improving End-to-End Models For Speech Recognition](https://ai.googleblog.com/2017/12/improving-end-to-end-models-for-speech.html)

The LAS architecture consists of 3 components. The listener encoder component, which is similar to a standard AM, takes the a time-frequency representation of the input speech signal, x, and uses a set of neural network layers to map the input to a higher-level feature representation, henc. The output of the encoder is passed to an attender, which uses henc to learn an alignment between input features x and predicted subword units {yn, … y0}, where each subword is typically a grapheme or wordpiece. Finally, the output of the attention module is passed to the speller (i.e., decoder), similar to an LM, that produces a probability distribution over a set of hypothesized words.


![Components of the LAS End-to-End Model.
](https://4.bp.blogspot.com/-D26UVY-JPh4/WjK9bo6LVtI/AAAAAAAACRk/ABz4VpV0uvUywryKqaaIXgFz4w-JukTegCLcBGAs/s640/image1.png "Components of the LAS End-to-End Model.
")

Components of the LAS End-to-End Model.


------

**This repository contains:**

1. [模型代码](core)复线论文的算法模型.
2. [创建 vocab 文件](generate_vocab_file.py), 使用该方法来生成自己的 vocab 文件 for [数据集](dataset).
3. [训练代码](train_asr.py) 来训练模型.
4. [验证代码](test_asr.py) 来验证模型.

------

## **内容列表**

- [**LAS_Mandarin_PyTorch**](#las_mandarin_pytorch)
  - [**Listen-Attend-Spell**](#listen-attend-spell)
    - [**谷歌博客主页**](#谷歌博客主页)
  - [**内容列表**](#内容列表)
  - [**依赖**](#依赖)
  - [**用法**](#用法)
    - [**预处理**](#预处理)
    - [**训练**](#训练)
    - [**验证**](#验证)
  - [**预训练模型**](#预训练模型)
    - [**英文**](#英文)
    - [**中文普通话**](#中文普通话)
  - [**Demo**](#demo)
  - [**Star-History**](#star-history)
  - [**引用**](#引用)
  - [**License**](#license)


------


## **依赖** 

```bash
pip install -r requirements.txt
```
## **用法**

### **预处理**

首先, 基于数据集的 transcripts 文件生成vocab 文件. 请参考 代码 [generate_vocab_file.py](generate_vocab_file.py). 如果你想训练 aishell 数据集, 你可以直接使用我写好的 [generate_vocab_file_aishell.py](generate_vocab_file_aishell.py).


```python
python generate_vocab_file_aishell.py --input_file $DATA_DIR/data_aishell/transcript_v0.8.txt --output_file ./aishell_vocab.txt --mode character --vocab_size 5000
```

它将创建好一个 vocab 文件， 在目录下命名为 **aishell_vocab.txt**.


### **训练** 

在训练之前, 需要重写自己的dataset加载器的代码 in package [dataset](dataset).

如果想使用我写好的aishell dataset 的加载器代码, 需要注意数据集里的 transcripts file 的路径配置，见 [data/aishell.py](dataset/aishell.py) 的第26行:

```python
src_file = "/data/Speech/SLR33/data_aishell/" + "transcript/aishell_transcript_v0.8.txt"
```

当一切都准备好. 

就可以开始训练了:

```bash
python main.py --config ./config/aishell_asr_example_lstm4atthead1.yaml
```

你可以自定义自己的配置文件, 可以参考 [config/aishell_asr_example_lstm4atthead1.yaml](config/aishell_asr_example_lstm4atthead1.yaml)

特别注意的变量: corpus's path & vocab_file

### **验证**

```bash
python main.py --config ./config/aishell_asr_example_lstm4atthead1.yaml --test
```

------

## **预训练模型**

### **英文**

### **中文普通话**

在数据集AISHELL-Dataset上训练的一个中文语音识别 ASR 模型的预训练权重文件

download from [Google Drive](https://drive.google.com/file/d/1Lcu6aFdoChvKEHuBs5_efNSk5edVkeyR/view?usp=sharing)

------

## **Demo**

推理:


```bash
python infer.py
```

------

## **Star-History**

![star-history](https://api.star-history.com/svg?repos=jackaduma/LAS_Mandarin_PyTorch&type=Date "star-history")

------

## **引用**

1. [**Listen, Attend and Spell**](https://arxiv.org/abs/1508.01211v2), W Chan et al.
2. [Neural Machine Translation of Rare Words with Subword Units](http://www.aclweb.org/anthology/P16-1162), R Sennrich et al.
3. [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503), J Chorowski et al.
4. [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](https://www.cs.toronto.edu/~graves/icml_2006.pdf), A Graves et al.
5. [Joint CTC-Attention based End-to-End Speech Recognition using Multi-task Learning](https://arxiv.org/abs/1609.06773), S Kim et al.
6. [Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM](https://arxiv.org/abs/1706.02737), T Hori et al.

------


## **License**

[MIT](LICENSE) © Kun