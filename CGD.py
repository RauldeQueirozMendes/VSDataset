from __future__ import absolute_import, division, print_function

import os
#os.environ["CUDA_VISIBLE_DEVICES"]="0"  # Do other imports now...

#IMPORT	
#import tensorflow as tf
import cv2
import numpy as np
import glob
import sys, os
import imageio
import matplotlib.pyplot as plt
import os
import time
import math
import warnings
import scipy
import argparse
import matplotlib as mpl
import argparse
import cv2
from scipy import interpolate
from scipy.interpolate import griddata
from math import (floor, ceil)
from tqdm import tqdm
from skimage import io

def join_dataset_path(filenames, dataset_path):
    timer = -time.time()
    filenames = [dataset_path + filename for filename in filenames]
    timer += time.time()
    print('time:', timer, 's\n')

    return filenames

def read_text_file(filename):
    print("\n[Dataloader] Loading '%s'..." % filename)
    try:
        data = np.genfromtxt(filename, dtype='str', delimiter=' ')
    except OSError:
        print("[OSError] Could not find the '%s' file." % filename)
        raise SystemExit

    # Parsing Data
    x = list(data[:, 0])
    y = list(data[:, 1])

    return x, y 


def load_img(filepath):
    image_input = imageio.imread(filepath)
    return image_input

if __name__ == '__main__':

    x, y = read_text_file('/home/raul/Downloads/01/pcd0100cpos.txt')
    
    img = load_img('/home/raul/Downloads/02/pcd0240r.png')

    print(img.shape)
    input("ok")

    #img[x[0:4], y[0:4], 0:3] = 127

    print(x)
    print(y)

    plt.figure(1)
    plt.imshow(img)
    plt.show()

print("Done.")

