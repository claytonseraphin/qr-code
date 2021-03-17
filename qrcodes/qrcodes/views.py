from django.shortcuts import render
from websites.models import Websites

def home_view(request):
    name = "Welcome to"

    obj = Websites.objects.get(id=1)


    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'home.html', context)
