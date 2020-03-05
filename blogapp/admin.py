from django.contrib import admin
from .models import Contact,Post,Comment
# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Comment)