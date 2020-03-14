from django.contrib import admin
from .models import Contact,Post,Comment,Video    
# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Video)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username','message','date_comment','post_id','active') 
    list_filter = ('active','date_comment')