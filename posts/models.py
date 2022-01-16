from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
