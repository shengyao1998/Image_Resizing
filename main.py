################################################################
#
# Authors                 : Yap Sheng Yao
# Program Name            : Image_Resizing
# Programming Languages   : Python
# Program Method          : Functional Programming (FP)
# Program Version         : Refer to GitHub
# Lastest Modifed Date    : 26 Oct 2022
#
################################################################


#--------------------------------------------------------------#
# Class (Function)'s Name   : main.py
#--------------------------------------------------------------#
# Main Execution of the Program


#################
#   Packages
#################
import os
import sys
import cv2
import glob
from pathlib import Path
from os import listdir
import matplotlib.pyplot as plt
import numpy as np


####################################################################
#   Input File Handling
####################################################################
absolute_path = os.path.dirname(os.path.abspath(__file__))
relative_path = "Input Files"
full_path = os.path.join("r", absolute_path, relative_path)

# print (absolute_path)
# print (relative_path)
# print (full_path)

for images in os.listdir(full_path):
    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        print (full_path)


####################################################################
#   Replace the Transparent bit with White Bit
####################################################################
# # Create a Mask
# trans_mask = img[:,:,2] == 0

# #replace areas of transparency with white and not transparent
# img[trans_mask] = [255, 255, 255]


# ####################################################################
# #   Image Shape Checking and Resizing
# ####################################################################
# result_ratio = 10
# img_dimension = img.shape
# img_ratio = img_dimension[1]/img_dimension[0]
# if img_ratio > result_ratio:
#     new_width = result_ratio * img_dimension[0]
#     cropped_region = int((img_dimension[1] - new_width)/2)
#     cropped_img = img[0:,cropped_region: (img_dimension[1]- cropped_region)]
#     # cv2.imshow("Display window2", cropped_img)
#     cv2.imwrite("Output Files/C# Icon.png",cropped_img)
# elif img_ratio < result_ratio:
#     new_width = result_ratio * img_dimension[0]
#     stich_region = int((new_width - img_dimension[1])/2)
#     stich_img = np.zeros([img_dimension[0],stich_region,3],dtype=np.uint8)
#     stich_img.fill(255)
#     combine_image = np.concatenate((stich_img, img, stich_img), axis=1)
#     # cv2.imshow("Display window2", combine_image)
#     cv2.imwrite("Output Files/C# Icon.png",combine_image)


# ####################################################################
# #   Output File Handling
# ####################################################################
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()