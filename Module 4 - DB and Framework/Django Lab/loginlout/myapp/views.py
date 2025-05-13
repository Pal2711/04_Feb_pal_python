from django.shortcuts import render,redirect
from .froms import * 
from .models import sinup
from django.contrib.auth import logout 

def index(request):
    if request.method == "POST":
        uem = request.POST.get("email")
        pas = request.POST.get("password")
        
        user = sinup.objects.filter(email=uem, password=pas)
        if user:
            print("Login Successful!")
            request.session["user"] = uem  # Save email in session
            return redirect("home")
        else:
            print("Error! Login failed...")

    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = sinup(request.POST)
        if form.is_valid():
            # for pass to cpass
            #if request.POST["password"]==request.POST[""]
            form.save()
            print("sinup DONE")
        else:
            print(form.errors)
        return redirect("/")
    return render(request, "signup.html")

def home(request):
    user = request.session.get("user") # fetch session data
    return render(request, "home.html", {"user":user})


def userlogout(request):
    logout(request)
    return redirect("/") 
