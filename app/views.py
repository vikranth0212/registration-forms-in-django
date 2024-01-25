from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from app.forms import *
from app.models import *
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate,login


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    #checking post method is activated or not

    if request.method=="POST" and request.FILES:
        ufd=UserForm(request.POST)
        #for data request.POST is enough
        pfd=ProfileForm(request.POST,request.FILES)
        #for data and files or for only files we need to use
        #request.POST and request.FILES is mandatory

        #to convert non modified function data objects to modified 
        #we need to give commit=False

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
            
            #sending the registration mail to user
            send_mail(
                'registration',
                'registration successfull',
                'vikranthfullstack@gmail.com',
                [MUFDO.email],
                fail_silently=False
            )
            # send_mail(1.'subject of mail in str',2.'msg in str'
            # 3.'from mail id in str i.e it is application or company mail id'
            #4. 'user mail id who is signup from html page we need to give in list'
            # it is coming in user object format in string
            # if we are giving manually we need to give in str format
            # 5.fail_silently=True it will handle error and it will not show error
            # if we five False it will not handle and throw error



            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('invalid')
            
    return render(request,'registration.html',d)


#Home page
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username} 
        return render(request,'home.html',d)
    return render(request,'home.html')       


#login
def user_login(request):
    if request.method=='POST':
        username=request.POST['un'] 
        password=request.POST['pw']  

        AUO=authenticate(username=username,password=password) 

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid credentials')
    return render(request,'user_login.html') 

# @login_required
# def profile_display(request):
#     un=request.session.get('username')
#     UO=User.objects.get()