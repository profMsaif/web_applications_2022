from blog.models import Post
from django.shortcuts import  render, redirect
from blog.forms import NewUserForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("blog:home")