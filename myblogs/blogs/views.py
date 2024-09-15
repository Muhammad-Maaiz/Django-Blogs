from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogs.models import Post

# Create your views here.
@login_required(login_url="login")
def add_blog(request):
    result = ""
    if request.method=="POST":
        blog_title = request.POST.get('blog_title')
        blog_author = request.user
        blog_content = request.POST.get('blog_content')
        blog_image = request.FILES.get('blog_image')
        blog_detail = Post(blog_title=blog_title,blog_author=blog_author,blog_content=blog_content,blog_image=blog_image)
        blog_detail.save()
        result = "Blog Added Successfully"
    
    return render(request, 'addblogs.html', {'result':result})

@login_required(login_url="login")
def update_blog(request, id):
    updateblog = Post.objects.get(id=id)  

    if request.method == "POST":
        blog_title = request.POST.get('blog_title')
        blog_content = request.POST.get('blog_content')
        
        # Updating the blog with new data
        updateblog.blog_title = blog_title
        updateblog.blog_content = blog_content
        updateblog.save()
        return redirect('blogsdetail',id=id)

    return render(request, 'updateblogs.html', {'updateblog': updateblog})

@login_required(login_url="login")
def delete_blog(request,id):
    blog = Post.objects.get(id=id)  
    if request.method=="POST":
        blog.delete()
        return redirect('home')  

    return render(request, 'deleteblogs.html',{'blog':blog})