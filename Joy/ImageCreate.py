# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:52:02 2022

@author: Sai Prathap
"""

import numpy as np
from PIL import Image
array = np.zeros([100,200,3] , dtype = np.uint8)
array[:,:100] = [255,128,0]
array[:,100:] = [0,0,255]
img = Image.fromarray(array)
img.save('test.png')