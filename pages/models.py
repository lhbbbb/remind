from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    