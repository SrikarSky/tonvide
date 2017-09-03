from PIL import ImageFilter
import numpy as np
from PIL import Image


def blur_image(image, radius, outImg):
        FILENAME = image
        imgNuts = Image.open(FILENAME)

        #Higher the value - more the blur. Example: 10
        imgNuts = imgNuts.filter(ImageFilter.GaussianBlur(radius))
        imgNuts = imgNuts.rotate(180)
        imgNuts.save(outImg)

img_in = 'IMG_9263'
img_out = img_in + '_b'
img_in_ext = img_in + '.JPG'
img_out_ext = img_out + '.JPG'

blur_image(img_in_ext, 15, img_out_ext)
#imgOut.save(img_out_ext)
