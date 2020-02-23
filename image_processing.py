import matplotlib.pyplot as plt
from skimage import io
from skimage import color
import cv2
# 0f1f896d9ae5a04752d3239c690402c022db4d72c0d2c087d73380896f72c466 was /
# file used for test outputs, any jpg file will work


def rgb2gray(name):
    file_name = name + '.jpg'
    #img = color.rgb2gray(io.imread(file_name))
    #plt.imshow(img)
    #plt.show()
    original = cv2.imread(file_name)
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

    cv2.imshow('Original image', original)
    cv2.imshow('Gray image', gray)

    #cv2.imwrite('gray_' + file_name, gray)

    # argument in milliseconds as wait delay for any key event, '0' defaulting to indefinite wait time
    cv2.waitKey(0)
    # close created windows
    #cv2.destroyAllWindows()


def resize_PAR(name, scale_percent = 80): # preserving aspect ratio
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    print('Original Dimensions: ', original.shape)
    length = int(original.shape[0] * scale_percent / 100)
    width = int(original.shape[1] * scale_percent / 100)
    dimensions = (length, width)
    resized = cv2.resize(original, dimensions, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions: ', resized.shape)

    cv2.imshow("Resized Image", resized)
    cv2.imwrite('resize_PAR' + file_name, resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(name, new_length, new_width):
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    print('Original Dimensions: ', original.shape)

    dimensions = (new_length, new_width)
    resized_file_name = 'resize_' + str(new_length) + 'x' + str(new_width) + "_" + file_name

    resized = cv2.resize(original,dimensions, interpolation = cv2.INTER_AREA)

    print('Resized Dimenesions: ', resized.shape)

    cv2.imshow("Resized Image", resized)
    cv2.imwrite(resized_file_name, resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def invert(name):
    file_name = name + '.jpg'
    original = cv2.imread(file_name)
    inverted = cv2.bitwise_not(original)

    cv2.imshow("Inverted Image", inverted)
    cv2.imwrite('invert_' + file_name, inverted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    file_name = input("Enter file name")
    #rgb2gray(file_name)
    #resize_PAR(file_name, 150)
    resize(file_name, 256, 256)
    # invert(file_name)

main()