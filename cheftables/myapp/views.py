from django.http import HttpResponse
from django.shortcuts import render

from .forms import LogForm

def home(request):
    return HttpResponse("<h1>Welcome To lemon squeeezy</h1>")

def log_form(request):
    form=LogForm()

    if request.method=="POST":
        form=LogForm(request.POST)
        if form.is_valid():
            form.save()

    context={"form":form}
    return render(request,"home.html",context)