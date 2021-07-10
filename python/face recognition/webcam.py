import cv2
import numpy as np 

#thư viện khuôn mặt
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0) # để truy cập vào camera

# vòng lặp để nó hiển thị liên tục
while(True):
  ret,frame=cap.read() # lấy dữ liệu liên tục từ camera, biến ret(sẽ trả lời true nếu truy cập thành công), frame là dữ liệu lấy từ webcam 
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # chuyển về ảnh xám
  face=face_cascade.detectMultiScale(gray)    
  for(x,y,w,h)in face:                        # tạo hình vuông trên mặt
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)   # (x,y) là chiều tịnh tiến của hình vuông, (0,0,255) màu hình vuông là đỏ,1 là độ dày hình vuông
  cv2.imshow('detecting face',frame)
  if cv2.waitKey(1) & 0XFF == ord('q'): #điều kiện thoát khỏi vòng lặp while , bấm q để thoát
        break;
# giải phóng bộ nhớ và hủy       
cam.release()
cv2.destroyAllWindows()