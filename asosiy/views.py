from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate,login , logout
from django.contrib import messages


def plans(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Plan.objects.create(
                sarlavha=request.POST['s'],
                batafsil=request.POST['b'],
                holat=request.POST['h'],
                vaqt=request.POST['v'],
                foydalanuvchi=request.user
            )
            return redirect('plans')
        content = {
            'plans': Plan.objects.filter(foydalanuvchi = request.user)
        }
        return render(request,'index.html',content)
    return redirect("/")

def plan_ochir(request,son):
    if request.user.is_authenticated:
        Plan.objects.filter(id=son, foydalanuvchi=request.user).delete()
    return redirect("plans")

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['l'],
            password = request.POST['p']
        )
        if user is None:
            messages.error(request,'Login yoki parolda xatolik bor')
            return redirect('login')
        login(request,user)
        return redirect("/plans/")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method == 'POST' and request.POST.get('p') == request.POST.get('p2'):
        User.objects.create_user(
            username = request.POST.get('l'),
            password = request.POST.get('p'),
        )
        return redirect("login")
    return render(request,'register.html')
