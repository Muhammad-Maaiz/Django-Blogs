from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
    blog_created_at = models.DateTimeField(auto_now_add=True)