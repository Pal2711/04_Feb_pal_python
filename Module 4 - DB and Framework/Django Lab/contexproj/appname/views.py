from django.shortcuts import render
import random
# Create your views here.

n = 1
def index(request):
    global n
    n += 1
    name = "pal"
    #num = random.randint(85,893)
    num = n
    return render(request, 'index.html',{"nm":name,"num":num})
