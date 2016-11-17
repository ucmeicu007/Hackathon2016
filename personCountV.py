import imutils
import cv2, os

face_cascade = cv2.CascadeClassifier('./opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
stcnt=50
ofcnt=0

while True:
	(grabbed, frame) = camera.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(frame, 1.10, 5, cv2.CASCADE_SCALE_IMAGE,(80,80))
	fcnt = len(faces)
	if fcnt > 0:
		faces[:,2:] += faces[:,:2]
	if stcnt > 2000:
		stcnt=0
	if stcnt >= 30 and fcnt <> ofcnt:
		ofcnt = fcnt
		stcnt = 0
	else:
		stcnt +=1

	ps = 'I see there is ' + `ofcnt`+' of you...' 
	for x1, y1, x2, y2 in faces:
		cv2.rectangle(frame, (x1,y1),(x2,y2),(127,255,0),2)
	cv2.putText(frame,ps,(10,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,255),2)
	cv2.imshow('image',frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
                break

camera.release
cv2.destroyAllWindows()
