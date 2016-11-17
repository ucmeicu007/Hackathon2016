import sys, cv2

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

def main():
    Camera = cv2.VideoCapture(0) 	
    while True:
    	# read images as 2D arrays (convert to grayscale for simplicity)
    	(grabbed, frame) = Camera.read()
	cv2.putText(frame,"Press 's' to start",(10,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255,0,0),2)
	cv2.imshow('EAD Cam', frame)
    	key = cv2.waitKey(1) & 0xFF
	if key == ord("s"):
		grabbed, frame = Camera.read()
    		img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		str2 = ""
		while True:
    			(grabbed, frame) = Camera.read()
    			img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# compare
    			n_m, n_0 = compare_images(img1, img2)
    			#print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
    			#print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size
    			if (n_0*1.0/img1.size) >= 0.005:
				str2 = "Warning: Anomalies detected..."
				ssize = 1.0
			else:
				str2 = ""
				ssize = 0.8
		    	key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				break
			cv2.putText(frame,str2,(10,440),cv2.FONT_HERSHEY_SIMPLEX, ssize,(0,0,255),2)
			cv2.imshow('EAD Cam', frame)
    			
	if key == ord("q"):
		break

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

if __name__ == "__main__":
    main()