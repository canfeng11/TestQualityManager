from django.shortcuts import render,redirect
from django.contrib import auth
from QualityManager import forms
from QualityManager import models
def login(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect("/index/")
        else:
            msg="账号或密码错误"
    return render(request,"login.html",{"msg":msg})
def reg(request):
    reg_obj=forms.Reg()
    if request.method=="POST":
        reg_obj=forms.Reg(request.POST)
        if reg_obj.is_valid():
            clean_data=reg_obj.cleaned_data
            # models.UserInfo.objects.create_user(**clean_data)
            print(clean_data)
            return redirect("/login/")
    return render(request,"reg.html",{"reg_obg":reg_obj})
