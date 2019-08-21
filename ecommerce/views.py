from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model


def HomePage(request):
    return render(request,"home.html",{})

def LoginPage(request):

    form=LoginForm(request.POST or None)
    print("not auth")
    if form.is_valid():
        username=form.cleaned_data["username"]
        password=form.cleaned_data["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            #context['form']=LoginForm()
            print('auth')
            return redirect("/admin")
        else:
            print("error")
    context={
            "form":form,
            }
    return render(request,"auth/login.html",context)

User=get_user_model()
def RegisterPage(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data["username"]
        password=form.cleaned_data["password"]
        email=form.cleaned_data["email"]
        User.objects.create_user(username,email,password)
    context={
            "form":form,
            }
    return render(request,"auth/register.html",context)
