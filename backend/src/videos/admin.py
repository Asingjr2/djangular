from django.contrib import admin

from .models import Video

admin.site.register(Video)

class VideoAdmin(admin.ModelAdmin):
    list=display= ("name",)