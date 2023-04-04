import cv2
import matplotlib.pyplot as plt
import numpy

def dao_anh(img):
    return 255-img
def show_anh_dao():
    fig=plt.figure(figsize=(16,9))
    ax1,ax2=fig.subplots(1,2)
    
    img=cv2.imread('tien.jpg',0)
    ax1.imshow(img,cmap='gray')
    ax1.set_title("anh goc")

    img_new=dao_anh(img)
    ax2.imshow(img_new,cmap='gray')
    ax2.set_title("dao anh")
    plt.show()

if __name__ == '__main__':
    show_anh_dao()

