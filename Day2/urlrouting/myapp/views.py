from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Django Page!")


def dashboard(request):
    return redirect(home)

def add1(request, x, y):
    c = x + y
    return HttpResponse(f"The sum of {x} and {y} is: {c}")

def add2(request):
    x = request.GET.get('x')
    y = request.GET.get('y')    
    c = int(x) + int(y)
    return HttpResponse(f"The sum of {x} and {y} is: {c}")
