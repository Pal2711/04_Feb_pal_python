from django.shortcuts import render,redirect
from .forms import StudForm
from .models import StudInfo 

def index(request):
    if request.method == "POST":
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record inserted")
        else:
            print(form.errors)
    else:
        form = StudForm()
    
    return render(request, "index.html", {"form": form})

def showdata(request):
    stdata = StudInfo.objects.all()
    return render(request, "showdata.html", {"stdata": stdata})

def deletedata(request, id):
    stid = StudInfo.objects.get(id=id)
    StudInfo.delete(stid)
    return redirect("showdata")