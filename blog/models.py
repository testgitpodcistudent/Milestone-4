from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except self.image.url.DoesNotExist:
            url = ""
        return url
