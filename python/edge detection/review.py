import cv2 
import matplotlib.pyplot as plt 

fig=plt.figure(figsize=(16,9))
ax1,ax2=fig.subplots(1,2)

img=cv2.imread('bt.jpg',0)
new=cv2.Canny(img,100,100)

ax1.imshow(img,cmap='gray')
ax1.set_title("anh goc")

ax2.imshow(new,cmap='gray')
ax2.set_title("anh lay vien")

plt.show()