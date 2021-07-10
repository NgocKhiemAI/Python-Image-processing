import cv2 
import numpy as np
import random
import matplotlib.pyplot as plt 


def sp_noise(image,prob):
 
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


img=cv2.imread('tien.jpg',0)
new_img=sp_noise(img,0.01)

cv2.imshow('Display Image',new_img)
cv2.waitKey(0)
