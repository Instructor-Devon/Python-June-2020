from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Foo INDEX")

def create(request):
    return HttpResponse("This is Foo CREATE")