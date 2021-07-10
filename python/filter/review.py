import cv2 
import matplotlib.pyplot as plt 

img=cv2.imread('tien.jpg',0)
img_new=cv2.GaussianBlur(img,(5,5),0)
fig=plt.figure(figsize=(16,9))
ax1,ax2=fig.subplots(1,2)
ax1.imshow(img,cmap='gray')
ax2.imshow(img_new,cmap='gray')

plt.show()