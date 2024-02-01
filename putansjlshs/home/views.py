from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, template_name="index.html")


def about(request):
    return render(request, template_name="about.html")


def enrollment(request):
    return render(request, template_name="enrollment.html")


def offerings(request):
    return render(request, template_name="offerings.html")

def organizations(request):
    return render(request, template_name="organizations.html")

def signup(request):
    return render(request, template_name="signup.html")

def login(request):
    return render(request, template_name="login.html")

def sitemap(request):
    return render(request, template_name="sitemap.html")