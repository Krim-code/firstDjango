from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def create_post(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html',context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Success")
            return redirect('posts')
        else:
            messages.error(request,"Please check form")
            return render(request,'blog/post_form.html',{'form': form})
    else:
        return False


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
