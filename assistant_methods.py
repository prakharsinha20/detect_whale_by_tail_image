
import skimage
from skimage import transform, color
import skimage.io as io
import os

def grayscale_image_to_color(img):
    return skimage.color.gray2rgb(img)

def fetch_images(target):
     return [os.path.join('../input/'+target, f)
                for f in os.listdir('../input/'+target)
                if f.endswith(".jpg")]