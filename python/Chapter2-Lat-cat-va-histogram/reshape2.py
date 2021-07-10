import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img=cv2.imread('dolar.tif',0)

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j],width=8))

arr_bit_1=[]
for i in lst:
    arr_bit_1.append(int(i[7]))

arr_bit_2=[]
for i in lst:
    arr_bit_2.append(int(i[6]))

arr_bit_3=[]
for i in lst:
    arr_bit_3.append(int(i[5]))

arr_bit_4=[]
for i in lst:
    arr_bit_4.append(int(i[4]))

arr_bit_5=[]
for i in lst:
    arr_bit_5.append(int(i[3]))

arr_bit_6=[]
for i in lst:
    arr_bit_6.append(int(i[2]))

arr_bit_7=[]
for i in lst:
    arr_bit_7.append(int(i[1]))

arr_bit_8=[]
for i in lst:
    arr_bit_8.append(int(i[0]))   

img_bit_1=(np.array(arr_bit_1,dtype='uint8')*1).reshape(img.shape[0],img.shape[1])
img_bit_2=(np.array(arr_bit_2,dtype='uint8')*2).reshape(img.shape[0],img.shape[1])
img_bit_3=(np.array(arr_bit_3,dtype='uint8')*4).reshape(img.shape[0],img.shape[1])
img_bit_4=(np.array(arr_bit_4,dtype='uint8')*8).reshape(img.shape[0],img.shape[1])
img_bit_5=(np.array(arr_bit_5,dtype='uint8')*16).reshape(img.shape[0],img.shape[1])
img_bit_6=(np.array(arr_bit_6,dtype='uint8')*32).reshape(img.shape[0],img.shape[1])
img_bit_7=(np.array(arr_bit_7,dtype='uint8')*64).reshape(img.shape[0],img.shape[1])
img_bit_8=(np.array(arr_bit_8,dtype='uint8')*128).reshape(img.shape[0],img.shape[1])

fig=plt.figure(figsize=(16,9))
(ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)=fig.subplots(3,3)

ax1.imshow(img,cmap='gray')
ax1.set_title("anh goc")

ax2.imshow(img_bit_8,cmap='gray')
ax2.set_title("anh bit 8")

ax3.imshow(img_bit_6,cmap='gray')
ax3.set_title("anh bit 6")

ax4.imshow(img_bit_4,cmap='gray')
ax4.set_title("anh bit 4")

ax5.imshow(img_bit_2,cmap='gray')
ax5.set_title("anh bit 2")

ax6.imshow(img_bit_8 + img_bit_7,cmap='gray')
ax6.set_title("anh 7+8")

ax7.imshow(img_bit_4+img_bit_5,cmap='gray')
ax7.set_title("anh 4+5")

ax8.imshow(img_bit_6+img_bit_7+img_bit_8,cmap='gray')
ax8.set_title("anh 6+7+8")

ax9.imshow(img_bit_2+img_bit_3+img_bit_4,cmap='gray')
ax9.set_title("anh 2+3+4")

plt.show