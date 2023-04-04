import cv2
import numpy as np

def dao_anh(img):
    return 255-img
def nothing(x):
    pass
# create window
cv2.namedWindow("Tracking")
#Set up demensions of window
cv2.resizeWindow("Tracking",500,400)
#Create trackbar to monitor color
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    #read image
    frame = cv2.imread('cachua.png')
    # convert image BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # get current demensions of trackbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
# thresholding
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
# Return array with 255 = pixels in range, other pixels = 0 
    mask = cv2.inRange(hsv, l_b, u_b)
# Using logic mathematics and to return image 
    res = cv2.bitwise_and(frame, frame, mask=mask)
# Show image 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
#Press 0 to exit
    key = cv2.waitKey(1)
    if key == 0:
        break
cv2.destroyAllWindows()