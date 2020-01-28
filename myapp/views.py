from django.shortcuts import render,redirect
from .models import user
from math import ceil
from myapp.result import result1



msg3=''



cls_name=[]
cls_value=[]
global room_dict1

global total
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
        global total
        total=0

        if amca==''and nmca=='' and dmca=='' and amba=='' and nmba=='' and amph=='' and nmph=='' and amcy=='' and nmcy=='' and amby=='' and nmby=='' and amma=='' and nmma=='':

            str='Atleast one class should write examination'
            return render(request,'myapp/second.html',{'msg':str})

        else:
            if amca!='':
                amca=int(amca)
                total+=amca
                cls_name.append('amca')
                cls_value.append(amca)
            if nmca!='':
                nmca=int(nmca)
                total+=nmca
                cls_name.append('nmca')
                cls_value.append(nmca)
            if dmca!='':
                dmca=int(dmca)
                total+=dmca
                cls_name.append('dmca')
                cls_value.append(dmca)
            if amba!='':
                amba=int(amba)
                total+=amba
                cls_name.append('amba')
                cls_value.append(amba)
            if nmba !='':
                nmba=int(nmba)
                total+=nmba
                cls_name.append('nmba')
                cls_value.append(nmba)
            if amph!='':
                amph=int(amph)
                total+=amph
                cls_name.append('amph')
                cls_value.append(amph)
            if nmph!='':
                nmph=int(nmph)
                total+=nmph
                cls_name.append('nmph')
                cls_value.append(nmph)
            if amcy!='':
                amcy=int(amcy)
                total+=amcy
                cls_name.append('amcy')
                cls_value.append(amcy)
            if nmcy!='':
                nmcy=int(nmcy)
                total+=nmcy
                cls_name.append('nmcy')
                cls_value.append(nmcy)
            if amby!='':
                amby=int(amby)
                total+=amby
                cls_name.append('amby')
                cls_value.append(amby)
            if nmby!='':
                nmby=int(nmby)
                total+=nmby
                cls_name.append('nmby')
                cls_value.append(nmby)
            if amma!='':
                amma=int(amma)
                total+=amma
                cls_name.append('amma')
                cls_value.append(amma)
            if nmma!='':
                nmma=int(nmma)
                total+=nmma
                cls_name.append('nmma')
                cls_value.append(nmma)
            global r
            r = ceil(total/40)
            global msg3
            if r==1:
                msg3="slect one room"

            if r == 2:
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
    global total
    global room_dict1
    room_dict={}
    if request.method=='POST':
        var=request.POST.getlist("checks[]")
        count=0
        sp2 = 40
        sp4 = 40
        sp5 = 40
        sp6 = 40
        sp7 = 100

        room=0
        for i in var:
            if i=="2p7":
                room=room+100

            else:
                room=room+40
            room_dict[i] = "y"
        print(room)


        print(room_dict)
        msg4="Total "+str(total)+" students write the examination "
        if total>room and (room-total)<=39 :
            return render(request,"myapp/sucess.html",{'msg3':msg3},{"msg4":msg4})
        elif (room-total)>=40 and "2p7" not in var:
            return render(request,"myapp/sucess.html",{'msg3':"select required rooms only.you required "+msg3+"only"})
        else:
            room_dict1 = result1(cls_name, cls_value, room_dict)
            return render(request,'myapp/list2.html',{'dict':room_dict})

def sp2_view(request):
    global room_dict1
    return render(request,'myapp/sp2.html',{'dict':room_dict1['2p2']},{'room':'2p2'} )
def sp4_view(request):
    global room_dict1
    return render(request,'myapp/sp2.html',{'dict':room_dict1['2p4']},{'room':'2p4'})
def sp5_view(request):
    global room_dict1
    return render(request,'myapp/sp2.html',{'dict':room_dict1['2p5']},{'room':'2p5'})
def sp6_view(request):
    global room_dict1
    return render(request,'myapp/sp2.html',{'dict':room_dict1['2p6']},{'room':'2p6'})
def sp7_view(request):
    global room_dict1
    return render(request,'myapp/sp7.html',{'dict':room_dict1['2p7']},{'room':'2p7'})
