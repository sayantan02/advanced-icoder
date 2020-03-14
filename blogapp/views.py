from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Contact,Post,Comment,Video
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .forms import CommentForm

# Create your views here.
# this is my index page.
def index(request):
    return render(request, 'blogapp/index.html')
# this is home page.
def home(request):
    return render(request,'blogapp/home.html')
# this is contact page
def contact(request):
    return render(request,'blogapp/contact.html')
# this is contacts second page.
def contacts(request) :
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
    else:
        return redirect('error')
    return render(request,'blogapp/contact.html')
# this is about page.
def about(request):
    return render(request,'blogapp/about.html')
# this is search page.
def search(request):
    query=request.GET['query']
    if len(query) > 3 :
        if len(query) < 30 :
            
            allPosts = (Post.objects.filter(title__icontains=query) or 
                        Post.objects.filter(content__icontains=query) or
                        Post.objects.filter(author__icontains=query)
                        )
            if (len(allPosts))< 1:
                allVideos = (Video.objects.filter(title__icontains=query))
                if (len(allVideos))< 1:
                    params = {'allPosts':allPosts,'query':query}
                    return render(request,'blogapp/search.html',params)
                else:
                    params = {'allVideos':allVideos, 'query':query}
                    return render(request,'blogapp/searchvideos.html', params)
            else:
                params = {'allPosts':allPosts,'query':query}
                return render(request,'blogapp/search.html',params)
                
        else :
            messages.error(request, "Your Query should be under 72 characters")
            return redirect('Home')
    else :
        messages.error(request, "Your Query should be at least 4 characters.")
        return redirect('Home')
# signup page.
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
        
        if len(signupusername) > 15:
            messages.error(request,"username must be under 15 characters")
            return redirect('Home')
        
        if signuppassword != password1:
            messages.error(request,"passwords do not match")
            return redirect('Home')
        if User.objects.filter(username=signupusername).exists() :
            messages.info(request,"username already in use !")
            return redirect('Home')
        else:
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
# this is login page.
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
 # this is for logout 
def handleLogout(request):
    logout(request)
    messages.success(request, "successfuly logged out ")
    return redirect('Home')
    # error page
def errorpage(request):
    return render(request,'blogapp/errorpage.html')
    # blog page.

def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blogapp/blog.html',context)
# blogpost page.
def blogPost(request,slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.filter(slug=slug).first()
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.info(request,"Your comment has been successfuly added")
    else:
        comment_form = CommentForm()  
    contexts = {'posts':posts,'comments':comments,'new_comment':new_comment,'comment_form':comment_form}
    return render(request,"blogapp/blogpost.html",contexts)  
# this is for comments.
def allauthor(request,author) :
    post = Post.objects.filter(author=author)
    context = {'post':post}
    return render(request,"blogapp/authorpost.html",context)

# this is for videos.
def videos(request):
    videos = Video.objects.all()
    context = {'videos':videos}
    return render(request,'blogapp/videos.html',context)
    