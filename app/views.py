from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail

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

            send_mail(
                'registration',
                'registration successfull',
                'vikranth15.6.1995@gmail.com',
                ['MUFDO.email'],
                fail_silently=True
            )
            #send_mail('subject of mail in str','msg in str'
            #'from mail id in str i.e it is application or company mail id'
            #'user mail id who is signup from html page we need to give in list'
            #it is coming in user object format in string
            #if we are giving manually we need to give in str format
            #fail_silently=True it will handle error and it will not show error
            #if we five False it will not handle and throw error



            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('invalid')
            
    return render(request,'registration.html',d)