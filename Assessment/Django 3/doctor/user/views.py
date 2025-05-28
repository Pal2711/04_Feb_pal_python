from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.hashers import make_password
from django import forms

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        unm = request.POST.get("username")
        pas = request.POST.get("password")
        user = usersignup.objects.filter(username = unm , password = pas)
        if user:
            print("login Successfull!")
            return redirect("index")
        else:
            print("Errror login failld")
    return render(request, 'login.html')


def signup(request):
    msg = ""
    if request.method == 'POST':
        form = usersignupform(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            if usersignup.objects.filter(username=username).exists():
                msg = "Username already exists!"
                print("Username already exists!")
            else:
              
                password = form.cleaned_data.get("password")
                form.instance.password = make_password(password)
                
                # Save the user
                form.save()
                msg = "Signup successful!"
                print("Signup successful!")
                return redirect("login")
    else:
        form = usersignupform()

    return render(request, 'signup.html', {'form': form, 'msg': msg})
