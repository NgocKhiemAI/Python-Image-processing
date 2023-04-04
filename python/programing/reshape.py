import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 10
img = cv2.imread('vivi.jpg',0)

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j],width=8)) 
        
img_8_bit=[]
for i in range(lst):
    img_8_bit.append(int(i[0]))

img_7_bit=[]
for i in range(lst):
    img_7_bit.append(int(i[1]))

img_6_bit=[]
for i in range(lst):
    img_6_bit.append(int(i[3]))

img_5_bit=[]
for i in range(lst):
    img_6_bit.append(int(i[4]))
img_4_bit=[]
for i in range(lst):
    img_4_bit.append(int(i[5]))

img_3_bit=[]
for i in range(lst):
    img_3_bit.append(int(i[6]))

img_2_bit=[]
for i in range(lst):
    img_2_bit.append(int(i[7]))

img_1_bit=[]
for i in range(lst):
    img_1_bit.append(int(i[8]))

# tái tạo ảnh
img8=(np.array(img_8_bit,dtype='unit8')*128)*(reshape(img.shape[0],img.shape[1]))
img7=(np.array(img_7_bit,dtype='unit8')*64)*(reshape(img.shape[0],img.shape[1]))
img6=(np.array(img_6_bit,dtype='unit8')*32)*(reshape(img.shape[0],img.shape[1]))
img5=(np.array(img_5_bit,dtype='unit8')*16)*(reshape(img.shape[0],img.shape[1]))
img4=(np.array(img_4_bit,dtype='unit8')*8)*(reshape(img.shape[0],img.shape[1]))
img3=(np.array(img_3_bit,dtype='unit8')*4)*(reshape(img.shape[0],img.shape[1]))
img2=(np.array(img_2_bit,dtype='unit8')*2)*(reshape(img.shape[0],img.shape[1]))
img1=(np.array(img_1_bit,dtype='unit8')*1)*(reshape(img.shape[0],img.shape[1]))

# xuất ảnh ra
fig=plt.figure(figsize=(16,9))
(ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)=fig.subplots(3,3)

ax1.imshow(img8,cmap='gray')
ax1.set_title("mp 8 bit")

ax2.imshow(img7,cmap='gray')
ax2.set_title("mp 7 bit")

ax3.imshow(img6,cmap='gray')
ax3.set_title("mp 6 bit")

ax4.imshow(img5,cmap='gray')
ax4.set_title("mp 5 bit")

ax5.imshow(img4,cmap='gray')
ax5.set_title("mp 4 bit")

ax6.imshow(img3,cmap='gray')
ax6.set_title("mp 3 bit")

ax7.imshow(img2,cmap='gray')
ax7.set_title("mp 2 bit")

ax8.imshow(img1,cmap='gray')
ax8.set_title("mp 1 bit")

ax9.imshow(img,cmap='gray')
ax9.set_title("anh goc")
plt.show()