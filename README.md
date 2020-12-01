![GitHub](https://img.shields.io/github/license/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic) 
![GitHub language count](https://img.shields.io/github/languages/count/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/RauldeQueirozMendes/USP-VS-CP-Dataset/total)
![GitHub contributors](https://img.shields.io/github/contributors/RauldeQueirozMendes/USP-VS-CP-Dataset)
![GitHub Release Date](https://img.shields.io/github/release-date/RauldeQueirozMendes/USP-VS-CP-Dataset)

# Visual Servoing dataset
> [E. G. Ribeiro](eduardogr@usp.br), [R. Q. Mendes](raulmendes@usp.br) and [V. Grassi Jr](vgrassi@usp.br)

## :open_book: Description

> Summary

```
Dataset for visual servoing (VS) and camera pose estimation. 
The images were obtained by a manipulator robot with an eye-in-hand camera in different poses. 
The labels represent the camera pose. 
It is possible to obtain the absolute pose of the camera without any pre-processing of the dataset, as well as the relative pose between images through matrix transformations. 
One may also use the dataset to get the camera's 6DoF speeds so that the visual servo control between two images can be performed. 
Such speeds are already calculated through the classic PBVS law and made available in the VSLabels.txt file.
```

## :gear: Construction of the dataset

We tested the visual servoing dataset on a hardware with Python 3.5, Keras (), Tensorflow (), Ubuntu 16.04 operating system, Intel Core  i7-7700 processor with 8 cores of 3.6GHz and an Nvidia GPU GeForce GTX 1050 Ti. 

To train a model that can perform visual servoing on different target objects, without the need to design features, it is necessary to have a dataset that efficiently captures the attributes of the environment in which the robot operates, be representative of the VS task and diverse enough to ensure generalization. To this end, the data is collected by the robot Kinova Gen3 in a way that approximates the self-supervised approach. Human interventions are associated with the assembly of the workspace and the setup of the robot, which involves determining a reference pose from which the robot captures the images and labels them.

The robot is programmed to assume different poses from a Gaussian distribution centered in the reference pose, with different standard deviations. This approach is inspired by the work of Bateux et al. (), which do the same, yet using virtual cameras and homography instead of a real environment. The reference pose (mean of the distribution) and the sets of Standard Deviations (SD) assumed by the robot are presented in Table ().

<table>
    <caption>Gaussian distribution parameters to build the VS dataset</caption> 
    <thead>
        <tr>
            <th colspan="2" rowspan="2">Dimension</th>
            <th rowspan="2">Mean</th>
            <th colspan="3">Standard Deviation</th>
        </tr>
        <tr>
            <td>Mid</td>
            <td>High</td>
            <td>Low</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>Position [m]</td>
            <td>x</td>
            <td>0.288</td>
            <td>0.080</td>
            <td>0.030</td>
            <td>0.010</td>
        </tr>
        <tr>
            <td>y</td>
            <td>0.344</td>
            <td>0.080</td>
            <td>0.030</td>
            <td>0.010</td>
        </tr>
        <tr>
            <td>z</td>
            <td>0.532</td>
            <td>0.080</td>
            <td>0.030</td>
            <td>0.005</td>
        </tr>
        <tr>
            <td rowspan=3>Orientation [<sup>o</sup>]</td>
            <td>α</td>
            <td>175.8</td>
            <td>5.0</td>
            <td>2.0</td>
            <td>1.0</td>
        </tr>
        <tr>
            <td>β</td>
            <td>-5.5</td>
            <td>5.0</td>
            <td>2.0</td>
            <td>1.0</td>
        </tr>
        <tr>
            <td>γ</td>
            <td>90.0</td>
            <td>5.0</td>
            <td>2.0</td>
            <td>1.0</td>
        </tr>
    </tbody>
</table>

The SD choices take into account the expected displacement values that the robot must perform during the VS. In this way, the images obtained from a high SD help the network to understand the resulting changes in the image space when a large displacement is made by the robot. The instances obtained from a low SD enable the reduction of the error between the reference image and the current one when they are very close, for a good precision in steady state. The mean SD values help the network to reason during most of the VS execution. Two dataset instance examples and their respective labels are illustrated in Fig. ().

> Instance examples from the VS dataset. Generated from a Gaussian distribution with mean in the reference pose [x, y, z, α, β, γ]: (0.228m, 0.344m, 0.532m, 175.8<sup>o</sup>, -5.5<sup>o</sup>, 90.0<sup>o</sup>) - Source: Author.

![Image taken from camera in pose (0.326m, 0.356m, 0.503m, 178.0<sup>o</sup>, 1.1<sup>o</sup>, 91.5<sup>o</sup>)](https://github.com/RauldeQueirozMendes/VSDataset/blob/main/Instance_Examples/23.png)
> (a) Image taken from camera in pose (0.326m, 0.356m, 0.503m, 178.0<sup>o</sup>, 1.1<sup>o</sup>, 91.5<sup>o</sup>)

![Image taken from camera in pose (0.258m, 0.207m, 0.402m, -175.8<sup>o</sup>, -23.0<sup>o</sup>, 87.2<sup>o</sup>)](https://github.com/RauldeQueirozMendes/VSDataset/blob/main/Instance_Examples/26.png)
> (b) Image taken from camera in pose (0.258m, 0.207m, 0.402m, -175.8<sup>o</sup>, -23.0<sup>o</sup>, 87.2<sup>o</sup>)

<table>
    <caption>VS dataset: Composition and labels generation</caption> 
    <thead>
        <tr>
            <th rowspan="2">Description</th>
            <th colspan="4">Composition</th>
            <th rowspan="2">Generation</th>
        </tr>
        <tr>
            <td>Scenes</td>
            <td>High SD</td>
            <td>Mid SD</td>
            <td>Low SD</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Multiple objects</td>
            <td>4</td>
            <td>767</td>
            <td>630</td>
            <td>600</td>
            <td>361,315</td>
        </tr>
        <tr>
            <td>Single objects</td>
            <td>13</td>
            <td>877</td>
            <td>910</td>
            <td>780</td>
            <td>161,625</td>
        </tr>
        <tr>
            <td>Books</td>
            <td>2</td>
            <td>208</td>
            <td>210</td>
            <td>180</td>
            <td>62,935</td>
        </tr>
        <tr>
            <td>Framed map</td>
            <td>1</td>
            <td>140</td>
            <td>140</td>
            <td>120</td>
            <td>50,470</td>
        </tr>
        <tr>
            <td>Total</td>
            <td>20</td>
            <td>1,992</td>
            <td>1,890</td>
            <td>1,680</td>
            <td>636,345</td>
        </tr>
    </tbody>
</table>

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
This dataset may be used either for commercial or non-commercial applications. However, we do not provide any warranty (or assume liability) for the provided dataset. We encourage the readers to see the [license script](LICENSE) for terms.
