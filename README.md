# KaggleBME303
Kaggle project created for BME303 Introduction to Programming (Python/C++) in Spring 2019
Utilized Python libraries: scikit, numpy, Matplotlib, OpenCV, scipy

### Goal was to create algorithm to segment and count cancerous nuclei in provided library of 5000+ images

## Methods for standardizing images so they could eventually be used to train a convolutional neural network to identify cancer nuclei
### Color channel conversion
- rgb2gray
- histogram 
- invert (greyscale - if majority of blobs were light as opposed to dark on histogram)
### Size standardization
- resize (dimensions as arguments)
- resize_PAR (resizing while preserving target aspect ratio percentage)

## Counting Nuclei
### Blob_log function using surface formulas and thresholds to identify and count nuclei

**Results can be found in kaggle_data.png**
