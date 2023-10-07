
from django.shortcuts import render,HttpResponse,redirect
from sports.models import *
from django.contrib import messages

def home(request):
    return render(request,'home.html',)

def about(request):
    return render(request, 'about.html',)

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        links=request.POST.get('links')
        message=request.POST.get('message')
        date=request.POST.get('date')
        interest_game=request.POST.get('interest_game')
        skills=request.POST.get('skills')
        role=request.POST.get('role')
        mregistration.objects.create(
            name=name,
            email=email,
            links=links,
            message=message,
            date=date,
            interest_game=interest_game,
            skills=skills,
            role=role,
        )
        messages.success(request,'Successfully Registered.')
        return redirect('/')
    return render(request, 'registration.html',)

def user_data(request):
    messages.success(request,'To be accessed by authorized person only.')
    data=mregistration.objects.all()
    return render(request,'user_data.html',{'user_data':data})
   