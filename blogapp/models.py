from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    custom_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    desc = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'meaasge from - '+ self.name
        
class Post(models.Model) :
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    dateTime = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.title + ' by ' + self.author

class Comment(models.Model) :
    username = models.CharField(max_length=20)
    message = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-date_comment',)
    
    def __str__(self):
        return self.message

class Video(models.Model):
    title = models.CharField(max_length=70,blank=True)
    video_src = models.TextField(blank=True)
    height = models.CharField(max_length=7,default=210)
    width = models.CharField(max_length=7,default=315)
    def __str__(self):
        return self.title[0:25] + "..."
