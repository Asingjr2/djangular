from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Regex with period must be last so that other items are considered
    url(r'^api/videos/', include("videos.api.urls")),
    url(r'^.*',TemplateView.as_view(template_name="ang_home.html"), name="home" ),
]
