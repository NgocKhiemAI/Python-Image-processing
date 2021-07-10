import cv2 
import matplotlib.pyplot as plt

def change_gama(img,c,gama):
    return float(c) * pow(img,gama)
def show_anh():
    fig=plt.figure(figsize=(16,9))
    ax1,ax2=fig.subplots(1,2)

    img=cv2.imread('sanbay.jpg',0)
    ax1.imshow(img,cmap='gray')
    ax1.set_title("ảnh gốc")

    img_new= change_gama(img,1.0,3.0)
    ax2.imshow(img_new,cmap='gray')
    ax2.set_title("ảnh đã chuyển đổi gama")

    plt.show()
if __name__ == '__main__':
     show_anh()
