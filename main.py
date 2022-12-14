################################################################
#
# Authors                 : Yap Sheng Yao
# Program Name            : Image_Resizing
# Programming Languages   : Python
# Program Method          : Functional Programming (FP)
# Program Version         : Ver 1.0
# Lastest Modifed Date    : 29 Nov 2022
#
################################################################


#--------------------------------------------------------------#
# Class (Function)'s Name   : main.py
#--------------------------------------------------------------#
# Main Execution of the Program


################################################################
#               Import Modules, Packages
################################################################
import os
import sys
import cv2
import glob
from pathlib import Path
from os import listdir
import matplotlib.pyplot as plt
import numpy as np


################################################################
#         Replace the Transparent bit with White Bit
################################################################
def remove_trans_bit(img):
    # Create a Mask
    trans_mask = img[:,:,2] == 0
    #replace areas of transparency with white and not transparent
    img[trans_mask] = [255, 255, 255]
    return img

################################################################
#           Image Shape Checking and Resizing
################################################################
def resize(img):
    result_ratio = 10
    img_dimension = img.shape
    img_ratio = img_dimension[1]/img_dimension[0]
    if img_ratio > result_ratio:
        new_width = result_ratio * img_dimension[0]
        cropped_region = int((img_dimension[1] - new_width)/2)
        result_image = img[0:,cropped_region: (img_dimension[1]- cropped_region)]
        # cv2.imshow("Display window2", cropped_img)
        # cv2.imwrite("Output Files/C# Icon.png",result_image)
    elif img_ratio < result_ratio:
        new_width = result_ratio * img_dimension[0]
        stich_region = int((new_width - img_dimension[1])/2)
        stich_img = np.zeros([img_dimension[0],stich_region,3],dtype=np.uint8)
        stich_img.fill(255)
        result_image = np.concatenate((stich_img, img, stich_img), axis=1)
        # cv2.imshow("Display window2", combine_image)
        # cv2.imwrite("Output Files/C# Icon.png",result_image)
    return result_image

################################################################
#               Input File Handling
################################################################
if __name__ == "__main__":
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    relative_in_path = "Input Files\\"
    relative_out_path = "Output Files\\"
    full_path = os.path.join("r", absolute_path, relative_in_path)
    input_path = full_path.replace('\\', '/')

    for images in os.listdir(input_path):
        # check if the image ends with png or jpg or jpeg
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            image = cv2.imread(relative_in_path + images)
            image = remove_trans_bit(image)
            image = resize(image)
            cv2.imwrite(relative_out_path + images, image)

# k = cv2.waitKey(0)
# cv2.destroyAllWindows()