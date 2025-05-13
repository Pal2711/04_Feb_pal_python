from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudInfoForm , upadtaForm
from .models import StudInfo 

def index(request):
    if request.method == "POST":
        form = StudInfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record inserted")
            return redirect("showdata") 
        else:
            print(form.errors)
    else:
        form = StudInfoForm()
        
    return render(request, "index.html", {"form": form})

def showdata(request):
    stdata = StudInfo.objects.all()
    return render(request, "showdata.html", {"stdata": stdata})

def deletedata(request, id):
    stid = get_object_or_404(StudInfo, id=id)
    stid.delete()
    return redirect("showdata")

def updatedata(request, id):
    stid = get_object_or_404(StudInfo, id=id)
    
    if request.method == "POST":
        form = upadtaForm(request.POST, instance=stid)
        if form.is_valid():
            form.save()
            print("Record updated")
            return redirect("showdata") 
        else:
            print(form.errors)
    else:
        form = upadtaForm(instance=stid)
        
    return render(request, "updatedata.html", {"form": form, "id": stid})
