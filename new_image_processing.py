import numpy as np  #we use numpy for array manipulations
import Image    # we use Image to create, open, and save images
import matplotlib.pyplot as plt #used to display images
from skimage.feature import blob_log    #imports the Laplacian of Gaussian function for use in counting number of nuclei
import glob #used to consider things in an image as objects
from skimage.io import imread   #used to read an image


import cv2
# 0f1f896d9ae5a04752d3239c690402c022db4d72c0d2c087d73380896f72c466 was /
# file used for test outputs, any jpg file will work


def rgb2gray(name):
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

    plt.imshow(original)
    #cv2.imshow('Original image', original)
    plt.show()
    plt.imshow(gray, cmap='Greys_r')
    plt.show()

    gray_img = Image.fromarray(gray)
    gray_img.save('gray_' + file_name, cmap='Greys_r')

def resize_PAR(name, scale_percent = 80): # preserving aspect ratio
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    print('Original Dimensions: ', original.shape)
    length = int(original.shape[0] * scale_percent / 100)
    width = int(original.shape[1] * scale_percent / 100)
    dimensions = (length, width)
    resized = cv2.resize(original, dimensions, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions: ', resized.shape)

    resized_img = Image.fromarray(resized)

    plt.imshow(resized_img)
    plt.show()
    resized_img.save('resize_PAR' + file_name, cmap='Greys_r')


def resize(name, new_length=512, new_width=512):
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    print('Original Dimensions: ', original.shape)

    dimensions = (new_length, new_width)
    resized_file_name = 'resize_' + str(new_length) + 'x' + str(new_width) + "_" + file_name

    resized = cv2.resize(original,dimensions, interpolation = cv2.INTER_AREA)

    print('Resized Dimenesions: ', resized.shape)


    plt.imshow(resized)
    plt.show()

    resized_img = Image.fromarray(resized)
    resized_img.save('resized512x512_' + file_name, cmap='Greys_r')


def count_nuclei(name):
    img = Image.open(name + '.jpg') #defines img as the nuclei image we want to examine

    #displays original image
    #plt.imshow(img)
    #plt.show()

    pix_val = list(img.getdata())   #puts the values of each pixel from the nuclei image into a list
                                    #each pixel value is a list

    pix_val_size = len(pix_val)

    #iterates for each row (pixel)
    for i in range(pix_val_size):
        j = 0   #j must be 0 for proper use in the below if statement

        #if the pixel is not intense enough, sets the pixel to (0, 0, 0), or the color black
        if pix_val[i] < 100:
            pix_val[i] = 0

        #otherwise, the pixel is set to 255, or the color white
        else:
            pix_val[i] = 255

    true_img = Image.new(img.mode, img.size)    #creates a new, blank image with same dimensions as the original one
    true_img.putdata(pix_val)   #fills the blank image with the new pixel values

    #displays the new images, with each nuclei highlighted red
    plt.imshow(true_img, cmap='Greys_r')
    plt.show()

    true_img.save('B&W.jpg')    #saves the new image as "B&W.jpg"



    ex_file = glob.glob('B&W.jpg')[0]   #sets ex_file to be the "red.jpg", which was created above, with objects in it (the nuclei)
    count_img = imread(ex_file, as_gray=True)   #converts the image to grayscale

    #calls the imported blob_log function, which uses surface formulas to find the number of objects in an image
    blobs_log = blob_log(count_img, min_sigma=13, max_sigma = 45, num_sigma= 10, threshold=.1)
        #min_sigma is the minimum size of an object we want to actually count as an object
        #max_sigma is the maximum size of an object we want to actually count as an object
        #num_sigma is the number of intermediate values of standard deviations to consider between min and max sigma
        #threshold is the lowest pixel intensity we want to consider when counting something as an object

    numrows=len(blobs_log)  # the length of blobs_log is the number of nuclei

    return print("Number of nuclei: ", numrows)    #prints the number of nuclei in the image

def main():
    file_name = input("Enter file name:")
    #rgb2gray(file_name)
    #resize_PAR(file_name, 150)

    #resize(file_name)
    count_nuclei(file_name)

main()