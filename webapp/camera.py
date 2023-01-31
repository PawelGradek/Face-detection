import cv2,os
from django.conf import settings
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()



class VideoCamera2(object):
	def __init__(self, pk):
		self.video = cv2.VideoCapture(0)
		self.pk = pk

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, img = self.video.read()
		
		
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
		
		if self.pk == 1:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # sobelx
		if self.pk == 2:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # sobely
		if self.pk == 3:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # sobelxy
		
		edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 
				
		frame_flip = cv2.flip(sobel,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

class VideoCamera2(object):
	def __init__(self, pk):
		self.video = cv2.VideoCapture(0)
		self.pk = pk

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, img = self.video.read()
		
		
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
		
		if self.pk == 1:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # sobelx
		if self.pk == 2:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # sobely
		if self.pk == 3:
			sobel = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # sobelxy
		
		edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 
				
		frame_flip = cv2.flip(sobel,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()
		