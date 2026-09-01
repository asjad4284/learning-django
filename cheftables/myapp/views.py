from django.http import HttpResponse
from django.shortcuts import render
from .forms import DemoForm


def home(request):
    # 1. Create an instance of the form
    my_form = DemoForm()
    
    # 2. Pass the form to the HTML template using a dictionary
    return render(request, "home.html", {"form": my_form})

def menu_items(request,dish):
    items={
        "Pasta":"This kind of pasta is made up of",
        "Cheesecake":"Cheesecake is a special type of dessert",
    }
    description=items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + description)

def item_number(request, item_number):
    return HttpResponse(f"This is item_number: {item_number}")
