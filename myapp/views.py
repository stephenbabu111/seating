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
            return render(request,'myapp/second.html')
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
        amph=request.POST.get("amph")
        nmph=request.POST.get("nmph")
        amcy=request.POST.get("amcy")
        nmcy=request.POST.get("nmcy")
        amby=request.POST.get("amby")
        nmby=request.POST.get("nmby")
        amma=request.POST.get("amma")
        nmma=request.POST.get("nmma")

        msg=''
        total=0
        if amca==''and nmca=='' and dmca=='' and amph=='' and nmph=='' and amcy=='' and nmcy=='' and amby=='' and nmby=='' and amma=='' and nmma=='':

            str='Atleast one class should write examination'
            return render(request,'myapp/second.html',{'msg':str})

        else:
            if amca!='':
                amca=int(amca)
                total+=amca
            if nmca!='':
                nmca=int(nmca)
                total+=nmca
            if dmca!='':
                dmca=int(dmca)
                total+=dmca
            if amph!='':
                amph=int(amph)
                total+=amph
            if nmph!='':
                nmph=int(nmph)
                total+=nmph
            if amcy!='':
                amcy=int(amcy)
                total+=amcy
            if nmcy!='':
                nmcy=int(nmcy)
                total+=nmcy
            if amby!='':
                amby=int(amby)
                total+=amby
            if nmby!='':
                nmby=int(nmby)
                total+=nmby
            if amma!='':
                amma=int(amma)
                total+=amma
            if nmma!='':
                nmma=int(nmma)
                total+=nmma
            print("the data is", amca, nmca, dmca, amba, nmba, amph, nmph, amcy, nmcy, amby, nmby, amma, nmma)
            print(type(amca))
            print("total:  ",total)
            return render(request,'myapp/sucess.html')