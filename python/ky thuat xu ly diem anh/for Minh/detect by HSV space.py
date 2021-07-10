import cv2
import numpy as np

def nothing(x):
    pass    
#Tạo cửa sổ tracking
cv2.namedWindow("Tracking")
#Tạo trackbar để theo dõi màu trong vùng màu HSV
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('cachua.png') # Đọc ảnh dưới dạng BGR

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# convert BGR to HSV
# Lấy giá trị hiện thời trên thanh trackbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
# tạo ngưỡng 
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b) # Hàm cv2 inRange sẽ trả về mảng trong đó với những pixel trong khoảng màu ở trên thì giá trị là 255 còn lại sẽ bằng 0
  
# Sử dụng hàm logic and để hiển thị kết quả
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 0:
        break

cv2.destroyAllWindows()