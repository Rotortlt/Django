from django.shortcuts import render

def main(request):
    contents = {"username": 'stive'}
    return render(request, "mainapp/index.html", contents)

def catalog(request):
    return render(request, "mainapp/Catalog.html")

def boxes(request):
    return render(request, "mainapp/Boxes.html")

def hanger(request):
    return render(request, "mainapp/Hanger.html")

def contacts(request):
    return render(request, "mainapp/Contact.html")


