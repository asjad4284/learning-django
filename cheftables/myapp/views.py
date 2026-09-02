from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm

def home(request):
    return HttpResponse("<h1>Welcome To lemon squeeezy</h1>")

def form_view(request):
    form=InputForm()
    context={"form":form}

    return render(request,"home.html",context)