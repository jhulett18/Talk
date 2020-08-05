from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {}) # String of HTML code
