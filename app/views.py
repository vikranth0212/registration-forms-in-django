from django.shortcuts import render

# Create your views here.
from app.forms import *

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo1':ufo,'pfo1':pfo}
    return render(request,'registration.html',d)