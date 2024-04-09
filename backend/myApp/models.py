from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .utils import *

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    content = FroalaField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog',default='1_tCLgoTtePAdJhGRImx-B-g.jpg')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = FroalaField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)