import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import random

# thêm nhiễu muối tiêu vào
def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
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
noise_img=sp_noise(img,0.05)

fig=plt.figure(figsize=(16,9))
(ax1,ax2),(ax3,ax4) =fig.subplots(2,2)

# dùng lọc gauss để lọc nhiễu
Gaussian_Blur=cv2.GaussianBlur(img,(5,5),0)       #dst = cv.GaussianBlur(	src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]	)
blur = cv2.bilateralFilter(img,9,75,75)            # lọc 2 chiều

ax1.imshow(img,cmap='gray')
ax1.set_title("anh goc")

ax2.imshow(noise_img,cmap='gray')
ax2.set_title("noise")

ax3.imshow(Gaussian_Blur,cmap='gray')
ax3.set_title("loc gauss")

ax4.imshow(blur,cmap='gray')
ax4.set_title("loc 2 chieu")
plt.show()