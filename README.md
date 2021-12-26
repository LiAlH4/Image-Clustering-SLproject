# Image clustering and semantic annotation via contrastive learning

This repo is based and modified by the paper:
> [**SCAN: Learning to Classify Images without Labels**](https://arxiv.org/pdf/2005.12320.pdf)

## Installation

The code runs with Pytorch on Linux system.
Assuming [Anaconda](https://docs.anaconda.com/anaconda/install/), the most important packages can be installed as:

```shell
conda install pytorch=1.4.0 torchvision=0.5.0 cudatoolkit=10.0 -c pytorch
conda install matplotlib scipy scikit-learn   # For evaluation and confusion matrix visualization
conda install faiss-gpu                       # For efficient nearest neighbors search 
conda install pyyaml easydict                 # For using config files
conda install termcolor                       # For colored print statements
```

We refer to the `requirements.txt` file for an overview of the packages in the environment we used to produce our results.

## Training

### Setup

The following files need to be adapted in order to run the code on your own machine:

- Change the file paths to the datasets in `utils/mypath.py`, e.g. `/path/to/cifar10`.
- Specify the output directory in `configs/env.yml`. All results will be stored under this directory.

Our experimental evaluation includes the following datasets: CIFAR10, CIFAR100-20, STL10 and ImageNet. The ImageNet dataset should be downloaded separately and saved to the path described in `utils/mypath.py`. Other datasets will be downloaded automatically and saved to the correct path when missing.

### Train model

The configuration files can be found in the `configs/` directory. The training procedure consists of the following steps:

- __STEP 1__: Solve the pretext task i.e. `simclr.py`
- __STEP 2__: Perform the clustering step i.e. `scan.py`
- __STEP 3__: Perform the self-labeling step i.e. `selflabel.py`

For example, run the following commands sequentially to perform our method on CIFAR10:

```shell
python simclr.py --config_env configs/env.yml --config_exp configs/pretext/simclr_cifar10.yml
python scan.py --config_env configs/env.yml --config_exp configs/scan/scan_cifar10.yml
python selflabel.py --config_env configs/env.yml --config_exp configs/selflabel/selflabel_cifar10.yml
```

The whole training and evaluation process costs around 12 hours on a single GTX1080 Ti GPU.
