[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bioflair-pretrained-pooled-contextualized/named-entity-recognition-on-species-800)](https://paperswithcode.com/sota/named-entity-recognition-on-species-800?p=bioflair-pretrained-pooled-contextualized)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bioflair-pretrained-pooled-contextualized/named-entity-recognition-ner-on-ncbi-disease)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-ncbi-disease?p=bioflair-pretrained-pooled-contextualized)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bioflair-pretrained-pooled-contextualized/named-entity-recognition-on-linnaeus)](https://paperswithcode.com/sota/named-entity-recognition-on-linnaeus?p=bioflair-pretrained-pooled-contextualized)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bioflair-pretrained-pooled-contextualized/named-entity-recognition-ner-on-bc5cdr)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-bc5cdr?p=bioflair-pretrained-pooled-contextualized)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bioflair-pretrained-pooled-contextualized/named-entity-recognition-ner-on-jnlpba)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-jnlpba?p=bioflair-pretrained-pooled-contextualized)
# BioFLAIR

This repository provides the code for fine-tuning BioFLAIR, a pretrained pooled contextualized embedding model for Biomedical Sequence Labeling tasks like NER. Please refer to our paper [BioFLAIR: Pretrained Pooled Contextualized Embeddings for Biomedical Sequence Labeling Tasks](https://arxiv.org/abs/1908.05760).

## Installation
BioFLAIR is built using [FLAIR](https://github.com/flairNLP/flair). Check out their repo for more information.
```
$ pip install flair
$ git clone https://github.com/shreyashub/BioFLAIR.git
```
## Datasets
We provide a pre-processed version of benchmark datasets as follows:
- NCBI
- BC5CDR (complete\chemicals\diseases)
- JNLPBA
- Species-800 
- LINNAEUS
## Fine-Tuning
Run `fine_tune.py` for fine-tuning proccess.

Just change the `data_folder = 'data/ner/DATASET_NAME'` in [fine_tune.py](https://github.com/shreyashub/BioFLAIR/blob/master/fine_tune.py#L7).
## Citation
```
@article{sharma2019bioflair,
  title={BioFLAIR: Pretrained Pooled Contextualized Embeddings for Biomedical Sequence Labeling Tasks},
  author={Sharma, Shreyas and Daniel Jr, Ron},
  journal={arXiv preprint arXiv:1908.05760},
  year={2019}
}
```
## Contact
Please email your questions or comments to Shreyas Sharma(`shreyas.rox101@gmail.com`)
