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

    # Created search method in model using compound queries with Q
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            qs = Video.objects.search(query)
        else:
            qs = Video.objects.all()
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
            qs = Video.objects.featured().search(query)
        else:
            qs = Video.objects.featured()
        return qs        


