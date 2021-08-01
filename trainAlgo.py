# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:09:57 2021

@author: Usuario
"""

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

x_l = "Naranja"

x = "Naranja"
y = "Pera"

sample_y_image = "train/y/green-pear-fruit-isolated-on-260nw-1165000129.jpg";

#tweak our images

datagen = ImageDataGenerator(
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                rescale=1.0/255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                fill_mode='nearest')

img = load_img(sample_y_image)

x = img_to_array(img)
x = x.reshape((1,) + x.shape)

i=0

for batch in datagen.flow(x,
                          batch_size=1,
                          save_to_dir='preview',
                          save_prefix=y,
                          save_format='jpg'):
    i+=1
    if i > 10:
        break
    
