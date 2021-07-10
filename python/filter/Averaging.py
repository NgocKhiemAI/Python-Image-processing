import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import random 

def CR_noise(image,prob):
    output=np.zeros(image.shape,np.uint8)
    thres=1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn=random.random()
            if rdn<prob:
                output[i][j]=0
            elif rdn >thres:
                output[i][j]=255
            else:
                output[i][j]=image[i][j]
    return output
fig= plt.figure(figsize=(16,9))
ax1,ax2=fig.subplots(1,2)

img= cv2.imread('tien.jpg',0)
noise_img=CR_noise(img,0.05)
blur_img=cv2.medianBlur(noise_img,5)

ax1.imshow(noise_img,cmap='gray')
ax1.set_title("anh goc")

ax2.imshow(blur_img,cmap='gray')
ax2.set_title('anh da loc')

plt.show()