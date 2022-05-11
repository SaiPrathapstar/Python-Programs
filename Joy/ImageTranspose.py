# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:36:22 2022

@author: Sai Prathap
"""

from PIL import Image
img  = Image.open('TypeSearchIcon.png')
transposed_image = img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_image.save('Corrected.png')
print("Flipping done")