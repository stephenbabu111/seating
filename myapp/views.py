from django.shortcuts import render,redirect
from .models import user
from math import ceil
msg3=''
dict={}
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
        sp2=40
        sp4=40
        sp5=40
        sp6=40
        sp7=100
        total=0

        if amca==''and nmca=='' and dmca=='' and amph=='' and nmph=='' and amcy=='' and nmcy=='' and amby=='' and nmby=='' and amma=='' and nmma=='':

            str='Atleast one class should write examination'
            return render(request,'myapp/second.html',{'msg':str})

        else:
            if amca!='':
                amca=int(amca)
                total+=amca
                dict["amca"]=amca
            if nmca!='':
                nmca=int(nmca)
                total+=nmca
                dict["nmca"]=nmca
            if dmca!='':
                dmca=int(dmca)
                total+=dmca
                dict["dmca"]=dmca
            if amba!='':
                amba=int(amba)
                total+=amba
                dict["amba"]=amba
            if nmba !='':
                nmba=int(nmba)
                total+=nmba
                dict["nmba"]=nmba
            if amph!='':
                amph=int(amph)
                total+=amph
                dict["amph"]=amph
            if nmph!='':
                nmph=int(nmph)
                total+=nmph
                dict["nmph"]=nmph
            if amcy!='':
                amcy=int(amcy)
                total+=amcy
                dict["amcy"]=amcy
            if nmcy!='':
                nmcy=int(nmcy)
                total+=nmcy
                dict["nmcy"]=nmcy
            if amby!='':
                amby=int(amby)
                total+=amby
                dict["amby"]=amby
            if nmby!='':
                nmby=int(nmby)
                total+=nmby
                dict["nmby"]=nmby
            if amma!='':
                amma=int(amma)
                total+=amma
                dict["amma"]=amma
            if nmma!='':
                nmma=int(nmma)
                total+=nmma
                dict["nmma"]=nmma
            r=ceil(total/40)
            global msg3
            if r==1:
                msg3="slect one room"
            if r==2:
                msg3="select two rooms"
            if r==3:
                msg3="select three rooms"
            if r==4:
                msg3="select four rooms"
            if r>=5:
                msg3="select all rooms"
            print("the data is", amca, nmca, dmca, amba, nmba, amph, nmph, amcy, nmcy, amby, nmby, amma, nmma)
            print(type(amca))
            print(dict)
            print("total:  ",total)
            return render(request,'myapp/sucess.html',{'msg3':msg3})
def list_view(request):
    if request.method=='POST':
        var=request.POST.getlist("check[]")
    if len(var)==0:
        return render(request,"myapp/sucess.html",{'msg3':msg3})
    else:
        for i in dict.keys():
            print(dict[i].keys())
    return render(request,'myapp/list.html')