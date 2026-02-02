from django.shortcuts import render, HttpResponse
from .models import Contact
from datetime import date
from django.contrib import messages

# Create your views here.

def index(request):
    context = {"variable": "Django"}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        print("This is a post request")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message, date.today())
        contact = Contact(name=name, email=email, phone=phone, message=message, date=date.today())
        contact.save()
        messages.success(request, 'Your form has been submitted successfully!')
        
    return render(request, 'contact.html')
