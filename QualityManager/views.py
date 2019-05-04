from django.shortcuts import render,redirect
from django.contrib import auth

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
