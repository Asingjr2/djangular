from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from videos.models import Video
from .serializers import VideoSerializer


class VideoList(generics.ListAPIView):
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer 
    permission_classes = []
    authentication_classes = []

    # Search return review using icontains method to see what contains query
    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = Video.objects.all()
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


class VideoDetail(generics.RetrieveAPIView):
    # Can override base queryset and method
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer 
    lookup_field = "slug"
    permission_classes = []
    authentication_classes = []

    def get_queryset(self):
        return Video.objects.all()


class VideoFeatured(generics.ListAPIView):
    serializer_class = VideoSerializer 
    permission_classes = []
    authentication_classes = []

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = all()
        if query:
            qs = Video.objects.filter(name__icontains=query).filter(featured=True)
        else:
            qs = Video.objects.filter(featured=True)
        return qs        


