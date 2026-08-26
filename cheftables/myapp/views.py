from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to lemon squeezy")

def menu_items(request,dish):
    items={
        "Pasta":"This kind of pasta is made up of",
        "Cheesecake":"Cheesecake is a special type of dessert",
    }
    description=items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + description)