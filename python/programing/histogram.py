import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('tien.jpg',0)# doc anh
img_equalized= cv.equalizeHist(img)# can bang anh

fig= plt.figure(figsize=(16,9))# tao vung anh
(ax1,ax2),(ax3,ax4)=fig.subplots(2,2)# tao 4 vung ve anh

#ve anh goc tai vung ve ax1 
ax1.imshow(img,cmap='gray')
ax1.set_title("anh goc")
 
# ve histogram cua anh goc
ax3.hist(img)
ax3.set_title("histogram anh goc")

# ve anh da equalized
ax2.imshow(img_equalized,cmap='gray')
ax2.set_title("equalized")

# ve histogram cua anh equalized
ax4.hist(img_equalized)
ax4.set_title("histogram cua equalized")

plt.show()