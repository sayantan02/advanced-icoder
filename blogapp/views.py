from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Post,Comment
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# from .models import Signing


# Create your views here.
def index(request):
    return render(request, 'blogapp/index.html')

def home(request):
    return render(request,'blogapp/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<4 or len(email)<3 or len(phone)<10 or len(content)<4 :
            messages.error(request,'Please Fill The Form Correctly')
        else:
            contact = Contact(name=name,email=email,phone=phone,desc=content)
            contact.save()
            messages.success(request,'Your Message has been Successfuly Sent !')
    return render(request,'blogapp/contact.html')
    
def about(request):
    return render(request,'blogapp/about.html')
    
def search(request):
    query=request.GET['query']
    if len(query) > 3 :
        if len(query) < 72 :
            
            allPosts = (Post.objects.filter(title__icontains=query) or 
                        Post.objects.filter(content__icontains=query))
            params = {'allPosts':allPosts,'query':query}
            return render(request,'blogapp/search.html',params)
        else :
            messages.error(request, "Your Query should be under 72 characters")
            return redirect('Home')
    else :
        messages.error(request, "Your Query should be at least 4 characters.")
        return redirect('Home')
def handleSignup(request):
    if request.method == 'POST':
        # get post parameters
        signupusername = request.POST ['signupusername']
        fname = request.POST ['fname']
        lname = request.POST ['lname']
        signupemail = request.POST ['signupemail']
        signuppassword = request.POST ['signuppassword']
        password1 = request.POST ['password1']
        # check for errorneous inputs
        if not signupusername.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return redirect('Home')
        
        if len(signupusername) > 10:
            messages.error(request,"username must be under 10 characters")
            return redirect('Home')
        
        if signuppassword != password1:
            messages.error(request,"passwords do not match")
            return redirect('Home')
        
        # create the user
        myuser = User.objects.create_user(signupusername, signupemail, signuppassword)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        myuser2 = authenticate(username=signupusername , password=signuppassword)
        login(request, myuser2)
        # print(myuser.first_name)
        messages.success(request,"Your ICoder account has Successfuly created !")
        return redirect('Home')
        
    else:
        return redirect('error')
    
def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername , password=loginpassword)
        if user is not None :
            login(request ,user)
            messages.success(request,"successfuly logged in ")
            return redirect('Home')
        else:
            messages.error(request,"invalid credentials, please try again later")
            return redirect('Home')
    else:
        return redirect('error')
    
def handleLogout(request):
    logout(request)
    messages.success(request, "successfuly logged out ")
    return redirect('Home')
    
def errorpage(request):
    return render(request,'blogapp/errorpage.html')


def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blogapp/blog.html',context)

def blogPost(request,slug):
    posts = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.all()
    contexts = {'posts':posts,'comments':comments}
    return render(request,"blogapp/blogpost.html",contexts)

def comment(request):
    if request.method == "POST":
        username = request.POST['username']
        message = request.POST['message']
        print("your username is"+username,message)
        return redirect('blogpost/')
    else:
        return redirect('error')
