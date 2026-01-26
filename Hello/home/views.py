from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {"variable": "Django"}
    return render(request, 'index.html',context)

def about(request):
    return HttpResponse("This is the About page.")

def contact(request):
    return HttpResponse("This is the Contact page.")


