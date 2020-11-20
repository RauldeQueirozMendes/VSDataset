![GitHub](https://img.shields.io/github/license/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic) 
![GitHub language count](https://img.shields.io/github/languages/count/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/RauldeQueirozMendes/USP-VS-CP-Dataset/total)
![GitHub contributors](https://img.shields.io/github/contributors/RauldeQueirozMendes/USP-VS-CP-Dataset)
![GitHub Release Date](https://img.shields.io/github/release-date/RauldeQueirozMendes/USP-VS-CP-Dataset)

# Visual Servoing dataset

## :open_book: Description

```
Dataset for visual servoing (VS) and camera pose estimation. 
The images were obtained by a manipulator robot with an eye-in-hand camera in different poses. 
The labels represent the camera pose. 
It is possible to obtain the absolute pose of the camera without any pre-processing of the dataset, as well as the relative pose between images through matrix transformations. 
One may also use the dataset to get the camera's 6DoF speeds so that the visual servo control between two images can be performed. 
Such speeds are already calculated through the classic PBVS law and made available in the VSLabels.txt file.
```

This is the implementation of the visual servoing dataset proposed in the following work to train Deep Learning models:

> [Real-Time Deep Learning Approach to Visual Servo Control and Grasp Detection for Autonomous Robotic Manipulation](https://arxiv.org/abs/2010.06544)
>
> [E. G. Ribeiro](eduardogr@usp.br), [R. Q. Mendes](raulmendes@usp.br) and [V. Grassi Jr](vgrassi@usp.br)

This dataset may be used either for commercial or non-commercial applications. However, we do not provide any warranty (or assume liability) for the provided dataset. We encourage the readers to see the [license script](LICENSE) for terms.

If you are planning to employ our dataset in your work please mind citing our paper:

```
@article{ribeiro2020real,
  title={Real-Time Deep Learning Approach to Visual Servo Control and Grasp Detection for Autonomous Robotic Manipulation},
  author={Ribeiro, EG and Mendes, RQ and Grassi Jr, V},
  journal={arXiv preprint arXiv:2010.06544},
  year={2020}
}
```
## :gear: Configuration

We tested the visual servoing dataset on a hardware with Python 3.5, Keras (), Tensorflow (), Ubuntu 16.04 operating system, Intel Core  i7-7700 processor with 8 cores of 3.6GHz and an Nvidia GPU GeForce GTX 1050 Ti. 

## :floppy_disk: Run

Firstly, to download the VS dataset you have to install the gdown and unzip dependencies as follows:

```shell
pip3 install gdown
sudo apt-get install unzip
```

Then, clone our repository to your PC:

```shell
git clone https://github.com/RauldeQueirozMendes/USP-VS-CP-Dataset.git
```

Finally, you have to run the download_vs_dataset.sh file in the VSDataset folder accordingly:

```shell
cd /path/to/USP-VS-CP-Dataset/VSDataset
sh download_vs_dataset.sh path_to_save_the_dataset
```

## :closed_lock_with_key: License
Please, see the [license script](LICENSE) for terms.
