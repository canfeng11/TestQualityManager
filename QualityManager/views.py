from django.shortcuts import render,redirect
from django.contrib import auth
from QualityManager import forms
from QualityManager import models
from django.contrib.auth.decorators import login_required
def login(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return render(request,"index.html")
        else:
            msg="账号或密码错误"
    return render(request,"login.html",{"msg":msg})

def reg(request):
    reg_obj=forms.Reg()
    if request.method=="POST":
        reg_obj=forms.Reg(request.POST)
        if reg_obj.is_valid():
            clean_data=reg_obj.cleaned_data
            clean_data.pop("confirm_pwd")
            models.UserInfo.objects.create_user(**clean_data)
            return redirect("/login/")
    return render(request,"reg.html",{"reg_obg":reg_obj})

@login_required
def index(request):
    return render(request,"index.html")

@login_required
def logout(request):
    auth.logout(request)
    return render(request,"login.html")

