from django.shortcuts import render
from home.models import Home


def home(request):
    homes = Home.objects.all()

    return render(request, "home.html", {"home": homes})
