from django.conf.urls import url

from .views import VideoList, VideoDetail, VideoFeatured


urlpatterns = [
    url(r'^$', VideoList.as_view(), name="list"),
    url(r'^featured/$', VideoFeatured.as_view()),
    url(r'^(?P<slug>[\w-]+)/*$', VideoDetail.as_view()),
    
]