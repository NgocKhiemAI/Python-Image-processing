import cv2 

img=cv2.imread('cachua.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh=100
img_binary=cv2.threshold(img_gray,thresh,255,cv2.THRESH_BINARY)[1]
cv2.imshow("anh nhi phan",img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows