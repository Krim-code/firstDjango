from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

# Create your views here.


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'users/login.html',context={'form':form})
