from django.shortcuts import redirect, render, HttpResponse
from .models import Contact
from datetime import date
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def checkAuthentication(request):
    username = request.session.get('Username')
    if not username:
        return redirect('login')
    return username

def index(request):
    username = checkAuthentication(request)
    context = {'Username': username} if username else {}
    return render(request, 'index.html', context)

def about(request):
    username = checkAuthentication(request)
    context = {'Username': username} if username else {}
    return render(request, 'about.html', context)

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
        
    username = checkAuthentication(request)
    context = {'Username': username} if username else {}
    return render(request, 'contact.html', context)

def login(request):
    if request.method == "POST":
        print("This is a post request of login")
        username = request.POST.get('username')
        password = request.POST.get('login_password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print("Authenticated Successfully")
            request.session['Username'] = username
            return redirect('home')
        else:
            # No backend authenticated the credentials
            print("Invalid Credentials, Please try again")
            messages.error(request, 'Invalid Credentials, Please try again')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        print("This is a post request of signup")
        username = request.POST.get('signup_username')
        email = request.POST.get('signup_email')
        password = request.POST.get('signup_password')
        print(username, email, password)
        # Here you would typically create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("User Created Successfully")
        messages.success(request, 'Your account has been created successfully!')
        return redirect('login')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')
            