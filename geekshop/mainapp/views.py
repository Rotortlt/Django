from django.shortcuts import render
from .models import Product

def main(request):
    contents = {"username": 'stive'}
    return render(request, "mainapp/index.html", contents)

def catalog(request):
    contents = {'products': Product.objects.all()}
    return render(request, "mainapp/Catalog.html", contents)

def boxes(request):
    content = {'products': Product.objects.all()}
    return render(request, "mainapp/Boxes.html", content)

def hanger(request):
    content = {'products': Product.objects.all()}
    return render(request, "mainapp/Hanger.html", content)

def contacts(request):
    return render(request, "mainapp/Contact.html")


