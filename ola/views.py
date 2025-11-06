from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hola Minna! Genki desuka?")
    return render(request, "ola/index.html")

def alex(req):
    return HttpResponse("Hi Alex.")

def marrie(req):
    return HttpResponse("Hi Marrie.")

def greet(req, name):
    # return HttpResponse(f"Hi, {name.capitalize()}.")
    return render(req, "ola/greet.html", {
        "name": name.capitalize()
    })