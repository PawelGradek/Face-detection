from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from webapp.camera import VideoCamera, VideoCamera2
# Create your views here.


def index(request):
	return render(request, 'webapp/index.html')

def face_detection(request):
	return render(request, 'webapp/face-detection.html')

def get_edges(request):
	return render(request, 'webapp/get-edges.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed2(request, pk):
	return StreamingHttpResponse(gen(VideoCamera2(pk)),
					content_type='multipart/x-mixed-replace; boundary=frame')
					