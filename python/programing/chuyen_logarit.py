import cv2 as cv 
import matplotlib.pyplot as plt

def change_logarit(img,c):
    return float(c) * cv.log(1.0+img)
def show_anh():
    fig=plt.figure(figsize=(16,9))
    ax1,ax2,ax3= fig.subplots(1,3)

    img=cv.imread('tien.jpg',0)
    ax1.imshow(img,cmap='gray')
    ax1.set_title("ảnh gốc")

    new_img=change_logarit(img,2)
    ax2.imshow(new_img,cmap='gray')
    ax2.set_title(" ảnh chuyển đổi logarit")
    
    ax3.hist(new_img)
    plt.show()
if __name__ == '__main__':
    show_anh()