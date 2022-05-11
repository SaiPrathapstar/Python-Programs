# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:44:19 2022

@author: Sai Prathap

"""
import cv2
img = cv2.imread('TypeSearchIcon.png')
#CLAHE Contrast limited adaptive histogram equalization
clahe = cv2.createCLAHE()
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
enh_img = clahe.apply(gray_img)
cv2.write('enhanced.png',enh_img)
print("Done")