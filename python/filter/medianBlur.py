import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


img= cv2.imread('cachua.png',0)
med_img=cv2.medianBlur(img,5)

fig= plt.figure(figsize=(16,9))
ax1,ax2=fig.subplots(1,2)

ax1.imshow(img,cmap='gray')
ax1.set_title("anh nhieu")

ax2.imshow(med_img,cmap='gray')
ax2.set_title("anh da loc nhieu")

plt.show()