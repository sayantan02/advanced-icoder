from django.db import models
from django.contrib.auth.models import User
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
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_id)
    