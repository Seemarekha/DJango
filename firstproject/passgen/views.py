from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World!!</h1> <br/><h2>My first Django project!</h2>")


def passgen(request):
    char = list("abcdefghijklmnopqrstuvwxyz")
