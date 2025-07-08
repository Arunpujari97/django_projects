from django.shortcuts import render
from register_app.models import register
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

def register_pages(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not name or not email or not password:
            return render(request, 'register.html', {'error': 'All fields are required'})

        if register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})

        hashed_password = make_password(password)
        register.objects.create(name=name, email=email, password=hashed_password)
        return render(request, 'login.html')
    return render(request,'register.html')

def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=register.objects.filter(email=email).first()
        if user and check_password(password, user.password): 
            return render(request,'dash_page.html')
        else:
            return render(request,'login.html',{'error':"pass and emails wrong"})
    return render(request, 'login.html')

def dash_page(request):
    return render(request,'dash_page.html')
