from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def registrationview(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='Accounts/registration.html'
    context={'form':form}
    return render(request,template_name,context)


def loginview(request):
    if request.method == "POST":
        U = request.POST.get('un')
        P = request.POST.get('ps')
        user = authenticate(username=U,password=P)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,'Invalid Credentials')
    return render(request,'Accounts/login.html')


def logoutview(request):
    logout(request)
    return redirect('login')