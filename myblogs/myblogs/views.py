from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from blogs.models import Post

def loginpage(request):
    result = ""
    if request.method == "POST":
        # Get username and password from login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check user is authenticate
        user=authenticate(request,username=username,password=password)
        # if authenticate then login and else show error
        if user is not None:
            login(request,user)
            return redirect('home')   # After login redirect to home page
        else:
            result = "Username or Password is Invalid"

    return render(request, 'login.html', {'result':result})

def signuppage(request):
    if request.method=="POST":
        # Get username,email and password from signup form
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Add User data to User Model
        user_data = User.objects.create_user(username,email,password)
        user_data.save()
        return redirect("login")         # redirect to login page

    return render(request, "signup.html")

def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def homepage(request):
    # display all blog posts
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

@login_required(login_url="login")
def blogsdetail(request,id):
    blogs = Post.objects.get(id=id)
    current_user = request.user
    return render(request, 'blogsdetail.html',{'blogs':blogs, 'current_user':current_user})