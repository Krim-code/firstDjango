from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
@login_required
def create_post(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html',context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Success")
            return redirect('posts')
        else:
            messages.error(request,"Please check form")
            return render(request,'blog/post_form.html',{'form': form})
    else:
        return False
@login_required
def edit_post(request,id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, id=id)

    if request.method == "GET":
        context = {'form': PostForm(instance=post),"id":id}
        return render(request,'blog/post_form.html', context)

    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'The post is update')
            return redirect('posts')
        else:
            messages.error(request,"Please check your data")
            return render(request,'blog/post_form.html', {"form": form})
@login_required
def delete_post(request,id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, id=id)
    context = {'post':post}
    if request.method == "GET":
        return render(request,'blog/post_confirm_delete.html',context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted")
        return redirect('posts')

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
