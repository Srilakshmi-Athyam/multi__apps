from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<h1>This is app2_first from app2<h1>')


def app2_second(request):
    return HttpResponse('<h1>This is app2_second from app2<h1>')