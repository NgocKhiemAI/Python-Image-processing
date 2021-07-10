import cv2 
import matplotlib.pyplot as plt 

img=cv2.imread('bt.jpg',0)
new=cv2.Canny(img,50,50)

fig=plt.figure(figsize=(16,9))
ax1,ax2=fig.subplots(1,2)

ax1.imshow(img,cmap='gray')
ax1.set_title("anh goc")

ax2.imshow(new,cmap='gray')
ax2.set_title("anh vien")

plt.show()