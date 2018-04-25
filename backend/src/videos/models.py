from django.db import models
from django.db.models.signals import pre_save
from django.db.models import Q

from .utils import unique_slug_generator


class VideoQuerySet(models.query.QuerySet):
    # Creating method to check items that are active
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        return self.filter(
            Q(name__icontains=query) |
            Q(slug__icontains=query) |
            Q(embed__icontains=query) 
            )


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    # Overridding built in method to filter for only items that are active
    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured().active()

    # Q generates object and uses && or either || to make compound searches
    def search(self, query):
        return self.get_queryset().search(query).active()

class Video(models.Model):
    name= models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    embed= models.CharField(max_length=200, help_text="Youtube embed code",null=True, blank=True)
    active = models.BooleanField(default=True)
    featured= models.BooleanField(default=False)
    timestop = models.DateTimeField(auto_now=True)

    objects = VideoManager()

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def video_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(video_pre_save_receiver, sender= Video)
