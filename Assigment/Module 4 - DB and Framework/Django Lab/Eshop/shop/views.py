from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    pdata = product_detail.objects.all()
    return render(request, "index.html", {'pdata': pdata})

def addproduct(request):
    print("Navigating to addproduct view")
    pname = product.objects.all()
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Product added")
            return redirect('index')
        else:
            print(form.errors)
    return render(request, "addproduct.html", {'pname': pname})

