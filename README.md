![GitHub](https://img.shields.io/github/license/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic) 
![GitHub language count](https://img.shields.io/github/languages/count/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/RauldeQueirozMendes/USP-VS-CP-Dataset?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/RauldeQueirozMendes/USP-VS-CP-Dataset/total)
![GitHub contributors](https://img.shields.io/github/contributors/RauldeQueirozMendes/USP-VS-CP-Dataset)
![GitHub Release Date](https://img.shields.io/github/release-date/RauldeQueirozMendes/USP-VS-CP-Dataset)

# Visual Servoing dataset

**Description**

```
Dataset for visual servoing and camera pose estimation. 
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

