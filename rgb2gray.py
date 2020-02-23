import sys
import os
from scipy import ndimage
import imageio.imwrite as imsave
import numpy as np

f = imsave.face()
imsave.imwrite('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

# rgb2gray
# def load_image(self, image_id):
#    image = skimage.io.imread(self.image_info[image_id]['path'])
#    skimage.color.rgb2gray(image)

