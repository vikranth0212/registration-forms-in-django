from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo1':ufo,'pfo1':pfo}

    if request.method=="POST" and request.FILES:
        ufd=UserForm(request.POST)
        #for data request.POST is enough
        pfd=ProfileForm(request.POST,request.FILES)
        #for data and files or for only files we need to use
        #request.POST and request.FILES is mandatory
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            #for default it is true and it will give non modified data
            #to modify the data we need to give commit=False
            

            pw=ufd.cleaned_data['password']
            # here we are getting pswd
            MUFDO.set_password(pw)
             # here we are getting encrypted pswd
            MUFDO.save()
            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            #here we are getting username column from another table i.e User table
            MPFDO.save()
            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('invalid')
            
    return render(request,'registration.html',d)