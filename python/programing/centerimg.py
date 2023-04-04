import cv2 
import imutils
img=cv2.imread('center.jpg',cv2.IMREAD_GRAYSCALE)
img_blured=cv2.GaussianBlur(img,(5,5),0)
thresh=cv2.threshold(img_blured,60,255,cv2.THRESH_BINARY)[1]
edge=cv2.Canny(thresh,50,50)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for i in cnts:
	# compute the center of the contour
	M = cv2.moments(i)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
 
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)