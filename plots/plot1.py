#!/usr/bin/env python
# encoding: utf-8
"""
plot1.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1.axes_size as Size

def make_heights_equal(fig, rect, ax1, ax2, pad):
    # pad in inches

    h1, v1 = Size.AxesX(ax1), Size.AxesY(ax1)
    h2, v2 = Size.AxesX(ax2), Size.AxesY(ax2)

    pad_v = Size.Scaled(1)
    pad_h = Size.Fixed(pad)



if __name__ == "__main__":

    fig1 = plt.figure()
    
    arr1 =  [[[0.27450980392156865, 0.5098039215686274, 0.7058823529411765],
[0.3607843137254902, 0.5686274509803921, 0.7372549019607844]],
[[0.5294117647058824, 0.6901960784313725, 0.803921568627451],
[0.8666666666666667, 0.9333333333333333, 0.9333333333333333]]]



    #arr1 = np.arange(12).reshape((2,2,3))
    #arr1 = np.arange(49).reshape((7,7))
    #arr2 = np.arange(20).reshape((5,4))

    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)

    ax1.imshow(arr1, interpolation="nearest")
    #ax2.imshow(arr2, interpolation="nearest")

    rect = 111 # subplot param for combined axes
    #make_heights_equal(fig1, rect, ax1, ax2, pad=0.5) # pad in inches


    plt.show()