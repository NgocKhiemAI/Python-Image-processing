import cv2 

img=cv2.imread('sanbay.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# câu lệnh để chuyển đổi sang ảnh xám

cv2.imshow("anh goc",gray) # xuất ảnh xám
cv2.waitKey(0)  # chờ
cv2.destroyAllWindows # xóa dữ liệu sau khi run
