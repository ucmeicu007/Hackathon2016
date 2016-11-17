import numpy as np
import cv2, os
from matplotlib import pyplot as plt

pillcnt = 0
img_rgb = cv2.imread('./pills.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
temp1 = cv2.imread('./pillback.jpg', 0)
w1, h1 = temp1.shape[::-1]

res = cv2.matchTemplate(img_gray, temp1, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
locthreshold = 7
loc = np.where( res >= threshold )
lptw=0
lpth=0
for pt in zip(*loc[::-1]):
	if (abs(lptw-pt[0]) > locthreshold and abs(lpth-pt[1]) > locthreshold):
		cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (255,0,0),1)
		pillcnt = pillcnt + 1
		lptw = pt[0]
		lpth = pt[1]

cv2.putText(img_rgb,`pillcnt` + ' counted',(700,750),cv2.FONT_HERSHEY_SIMPLEX, 1.1,(0,0,255),2)
cv2.imshow('EAD CAM',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
