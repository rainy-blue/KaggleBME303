import numpy as np  #we use numpy for array manipulations in counting nuclei in initially b&w image
import Image    # we use Image to create, open, and save images
import matplotlib.pyplot as plt #used to display images
from skimage.feature import blob_log    #imports the Laplacian of Gaussian function for use in counting number of nuclei
import glob #used to consider things in an image as objects
from skimage.io import imread   #used to read an image
import cv2  #used to read images and convert colored images to grayscale
# 0f1f896d9ae5a04752d3239c690402c022db4d72c0d2c087d73380896f72c466 was /
# file used for test outputs, any jpg file will work


#defines function for converting color image to grayscale
def rgb2gray(name):
    file_name = name
    original = cv2.imread(file_name)
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

    plt.imshow(gray, cmap='Greys_r')
    plt.show()

    gray_img = Image.fromarray(gray)
    gray_img.save('gray_' + file_name, cmap='Greys_r')

    return 'gray_' + file_name


#defines function for resizing an image while preserving aspect ratio
def resize_PAR(name, scale_percent = 80):
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

    resized_file_name = 'resize_PAR_' + file_name
    resized_img.save(resized_file_name, cmap='Greys_r')

    return resized_file_name


#defines function for resizing the image to 512x512
def resize(name, new_length=512, new_width=512):
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    print('Original Dimensions: ', original.shape)

    dimensions = (new_length, new_width)

    plt.imshow(original)
    plt.show()
    resized_file_name = 'resize_' + str(new_length) + 'x' + str(new_width) + "_" + file_name

    resized = cv2.resize(original, dimensions, interpolation=cv2.INTER_AREA)

    print('Resized Dimenesions: ', resized.shape)

    #displays the resized image
    plt.imshow(resized)
    plt.show()

    resized_img = Image.fromarray(resized)
    resized_img.save(resized_file_name, cmap='Greys_r')

    return resized_file_name    #returns the new file name


#defines a function for finding original height of the image
def find_orig_height(name):
    file_name = name + '.jpg'   #sets file name
    original = cv2.imread(file_name)    #reads the image
    orig_height, orig_width, channels = original.shape  #sets variables equal to the dimensions of the image
    return orig_height  #returns the original image height


#defines a function for finding the new height of the image
def find_new_height(name):
    #we will have the input be the resized image
    resized = cv2.imread(name)  #reads the resized image
    new_height, new_width, channels = resized.shape #sets variables equal to the dimensions of the image
    return new_height   #returns the height of the resized image


#defines function for counting the nuclei in an image that is in grayscale
def count_nuclei(name, new_height, original_height):
    img = Image.open(name) #defines img as the nuclei image we want to examine

    pix_val = list(img.getdata())   #puts the values of each pixel from the nuclei image into a list
                                    #each pixel value is a list

    pix_val_size = len(pix_val) #sets pix_val_size equal to the length of the data set of 1-channel pixel values

    #iterates for each row (pixel)
    for i in range(pix_val_size):
        j = 0   #j must be 0 for proper use in the below if statement

        #if the pixel is not intense enough, sets the pixel to (0, 0, 0), or the color black
        if pix_val[i] < 115:
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
    blobs_log = blob_log(count_img, min_sigma=14*new_height/original_height, max_sigma = 45*new_height/(2*original_height), num_sigma= 10*new_height/original_height, threshold=.1)
        #min_sigma is the minimum size of an object we want to actually count as an object
        #max_sigma is the maximum size of an object we want to actually count as an object
        #num_sigma is the number of intermediate values of standard deviations to consider between min and max sigma
        #threshold is the lowest pixel intensity we want to consider when counting something as an object

    numrows=len(blobs_log)  # the length of blobs_log is the number of nuclei

    return print("Number of nuclei: ", numrows)    #prints the number of nuclei in the image


#defines function for counting nuclei in an image that is not in grayscale
def count_nuclei_bw(name, original_height, new_height):
    img = Image.open(name)

    pix_val = list(img.getdata())

    array = np.asarray(pix_val)

    row = np.size(array, 0)

    for i in range(row):
        j = 0  # j must be 0 for proper use in the below if statement

        # if the pixel is not intense enough, sets the pixel to (0, 0, 0), or the color black
        if array[i, j] < 20 and array[i, j + 1] < 20 and array[i, j + 2] < 20:
            array[i, j] = 0
            array[i, j + 1] = 0
            array[i, j + 2] = 0

        # otherwise, the pixel is set to (255, 0, 0), or the color red
        else:
            array[i, j] = 255
            array[i, j + 1] = 0
            array[i, j + 2] = 0

    im_list = tuple(map(tuple, array))  #converts the array of new pixel values back into a tuple so that the tuple can be used to generate a new image
    true_img = Image.new(img.mode, img.size)
    true_img.putdata(im_list)

    # displays the new images, with each nuclei highlighted red
    plt.imshow(true_img)
    plt.show()

    true_img.save('red.jpg')  # saves the new image as "red.jpg"

    ex_file = glob.glob('red.jpg')[0]
    count_img = imread(ex_file, as_gray=True)

    blobs_log = blob_log(count_img, min_sigma=14*new_height/original_height, max_sigma=45*new_height/(2*original_height), num_sigma=10*new_height/original_height, threshold=.1)

    numrows = len(blobs_log)

    print("Number of nuclei: ", numrows)


#the main function, which calls the above function to resize the image, convert it to grayscale if necessary,
# and count the nuclei in it
def main():
    file_name = input("Enter file name:")   #asks user for the file name

    resized_dim = resize_PAR(file_name, 150)    #calls resize_PAR function to obtain a resized image
    #resized_dim = resize(file_name)            #calls resize function to obtain a resized image

    orig_height = find_orig_height(file_name)   # calls find_orig_height function to obtain the image's original height
    new_height = find_new_height((resized_dim)) #calls find_new_height function to obtain the resized image's height

    #count_nuclei(rgb2gray(resized_dim), new_height, orig_height)    #calls count_nuclei function to find the number of nuclei in the resized, grayscale image
    count_nuclei_bw(resized_dim, new_height, orig_height)  #calls count_nuclei_bw function to find the number of nuclei in the resized, initially black-and-white image


main()