from django.urls import path, include
from webapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('video_feed2/<int:pk>', views.video_feed2, name='video_feed2'),
    path('face_detection', views.face_detection, name='face-detection'),
    path('get_edges', views.get_edges, name='get-edges'),
    ]