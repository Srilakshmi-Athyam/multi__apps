from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return  HttpResponse("<h1>this is app1_first from app1</h1>")


def app1_second(request):
    return  HttpResponse("<h1>this is app1_second from app1</h1>")
