from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random


# 把所有的models都引进来

# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')


def Login_view(request):
    # 一般登录不会用get，因为get会暴露，所以使用的是post
    u = request.POST.get("users", '')
    p = request.POST.get("pwd", '')

    if u and p:
        c = PollsStudentinfo.objects.filter(stu_name=u, stu_psw=p).count()
        if c >= 1:
            return HttpResponse("login success")
        else:
            return HttpResponse("uncorrected")
    else:
        return HttpResponse("please input the username and password")


# register
def register_view(request):
    u = request.POST.get("users", '')
    p = request.POST.get("pwd", '')
    if u and p:
        stu = PollsStudentinfo(stu_name=u, stu_psw=p, stu_id=str(random.randrange(1111, 9999)))
        stu.save()
        return HttpResponse('register success')
    else:
        return HttpResponse('please input the username and password to register')


# click register
def toregister_view(request):
    return render(request, 'register.html')
