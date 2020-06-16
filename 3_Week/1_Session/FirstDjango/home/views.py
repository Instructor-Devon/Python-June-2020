from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "colors": ['red', 'blue', 'green', 'hacker-green']
    }
    return render(request, 'index.html', context)

def contact(request):
    return HttpResponse("Contact me!")

def about(request):
    return HttpResponse("More about me here!")

def colors(request, name):
    converted = name[0].upper() + name[1:]

    return HttpResponse(f"{converted} is a great color!")

def users(request, id):
    return HttpResponse(f"Page for User #{id}")

def create(request):
    print(request.POST)
    return redirect('/')