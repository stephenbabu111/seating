from django.shortcuts import render,redirect
from .models import user

# Create your views here.

def home_view(request):
    str=''
    return render(request,'myapp/login.html',{'msg':str})
def suc_conf(request):
    if request.method=='POST':
        print('login conf view is running')
        username=request.POST.get('username')
        password=request.POST.get('password')
        log=user.objects.filter(username=username,password=password).values('username','password')
        print(log)
        #print(log[0]['username'])
        str='myapp/sucess.html'
        str1=' '
        name=' '
        if not log:
            str1='username does not exist'
            str='please enter correct user name and password'
            return render(request,'myapp/login.html',{'msg':str})

        else:
            print('login was succesfull')
            return render(request,'myapp/sucess.html')
    return render(request,'myapp/forgot.html')
def forgot_view(request):
    msg='enter your username to get password'
    return render(request,'myapp/forgot.html',{'msg':msg})
def forgot2_view(request):
    print("running")
    msg=' '
    from myapp.forgot import send_message
    if request.method=="POST":
        print("this view is running")
        usernm=request.POST.get("username")
        print(usernm)
        user2=user.objects.filter(username=usernm)
        print(user2)
        if user2:
            user2 = user.objects.filter(username=usernm).values('phone', 'password')
            print(user2)
            phone=user2[0]['phone']
            password=user2[0]['password']
            print(phone,password)
            try:
                send_message(phone,password)

            except:
                msg='connection problem please try after some time'
            else:
                msg='password sent to your mobile ******'+phone[6:]
        else:
            msg='user not existed'
    return render(request,'myapp/forgot.html',{'msg':msg})
def class_select_view(request):
    return render(request,'myapp/second.html')
def class_select2_view(request):
    if request.method=='POST':
        print('the data view')
        amca=request.POST.get("amca")
        nmca=request.POST.get("nmca")
        dmca=request.POST.get("dmca")
        amba=request.POST.get("amba")
        nmba=request.POST.get("nmba")
        amp=request.POST.get("amp")
        nmp=request.POST.get("nmp")
        amc=request.POST.get("amc")
        nmc=request.POST.get("nmc")
        amb=request.POST.get("amb")
        nmb=request.POST.get("nmb")
        amm=request.POST.get("amm")
        nmm=request.POST.get("nmm")
        print("the data is",amca,nmca,dmca,amba,nmba,amp,nmp,amc,nmc,amb,nmb,amm,nmm )
        msg=''
        if amca.isalpha() or nmca.isalnum() or dmca.isalnum() or amba.isalnum() or nmba.isalnum() or amp.isalnum() or nmp.isalnum() or amc.isalnum() or nmc.isalnum() or amb.isalnum() or nmb.isalnum() or amm.isalnum() or nmm.isalnum():
            str='please enter a valid input'
            return render(request,'myapp/second.html',{'msg':str})
        else:
            return render(request,'myapp/sucess.html')