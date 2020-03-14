#This urls.py is made by Admin-Sayantan.
from django.urls import path
from blogapp import views
urlpatterns = [
    
         path('',views.index,name='Home'),

         path('home/' ,views.home,name='home page'),

         path('blog/' ,views.blog,name='Blog page'),

         path('blog/<str:slug>' ,views.blogPost,name='blogpost'),
         
         path('search/<str:slug>' ,views.blogPost,name='blogpost'),
         
         path('<str:author>' ,views.allauthor,name='allauthors'),
         
         path('contact/' ,views.contact,name='contactPage'),
         
         path('contacts/' ,views.contacts,name='contactPage'),

         path('about/' ,views.about,name='about_page'),
         
         path('signup/' ,views.handleSignup,name='handleSignup'),
         
         path('login/' ,views.handleLogin,name='handleLogin'),

         path('logout/' ,views.handleLogout,name='handleLogout'),
         
         path('search/' ,views.search,name='search-page'),
         
         path('error/' ,views.errorpage,name='error'),
         
         path('videos/',views.videos,name='videos-page'),
         
         path('/',views.blogPost,name='blogpost-comments'),
         
]