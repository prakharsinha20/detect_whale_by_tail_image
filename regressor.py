import skimage
from skimage import transform, data
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import tensorflow as tf
#from scikit-image import *


labels =[]
images = []
class_names = []
df_train = pd.read_csv('../input/train.csv')
class_names = list(set(df_train['Id'].tolist()))
print(class_names)
train_images = [os.path.join('../input/train', f)
                for f in os.listdir('../input/train')
                if f.endswith(".jpg")]
for f in train_images:
    img = skimage.data.imread(f)
    #img = tf.image.encode_jpeg(img)
    img = transform.resize(img, (28, 28))
    images.append(img)
    img_name = f.split('/')[-1]
    #print(df_train.loc[df_train['Image'] == img_name, 'Id'].iloc[0])
    labels.append(class_names.index(df_train.loc[df_train['Image'] == img_name, 'Id'].iloc[0]))
print(labels)
#images = images/255.0

