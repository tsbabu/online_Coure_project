from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from app.models import Student_data,Enroll_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')


def adlogin(request):
    user=request.POST.get('t1')
    pwd=request.POST.get('t2')
    user=authenticate(username=user,password=pwd)
    if user:
        login(request,user)
        if user.is_superuser:
            return render(request,'admin_login.html')
    else:
        messages.error(request,'incorrect')
        return render(request,'index.html',)


def schedule_class(request):
    return render(request,'addcourse.html')


def save(request):
    cname=request.POST.get('c1')
    faculty=request.POST.get('c2')
    cdate=request.POST.get('c3')
    c_time=request.POST.get('c4')
    fees=request.POST.get('c5')
    duratiion=request.POST.get('c6')
    try:
        Course(cname=cname,faculty=faculty,class_date=cdate,class_time=c_time,fees=fees,duration=duratiion).save()
        messages.success(request,'course add sucessfully')
        return render(request,'addcourse.html')
    except:
        messages.success(request,'something goeswrong')
        return render(request,'addcourse.html')


def viewall_schedules(request):
    qs=Course.objects.all()
    return render(request,'viewall_schedule.html',{'data':qs})


def update_course(request):
    no=request.GET.get('no')
    res=Course.objects.get(cno=no)
    return render(request,'update.html',{'data':res})


def course_update(request):
    cno=request.POST.get('c')
    cname = request.POST.get('c1')
    faculty = request.POST.get('c2')
    cdate = request.POST.get('c3')
    c_time = request.POST.get('c4')
    fees = request.POST.get('c5')
    duratiion = request.POST.get('c6')
    try:
        res=Course.objects.filter(cno=cno).update(cname=cname,faculty=faculty,class_date=cdate,class_time=c_time,fees=fees,duration=duratiion)
        qs=Course.objects.all()
        messages.success(request, 'data updated sucessfully')
        return render(request,'viewall_schedule.html',{'data':qs})
    except:
        qs=Course.objects.all()
        messages.success(request, 'update not sucessfully')
        return render(request,'viewall_schedule.html',{'data':qs})


def delete_course(request):
    cno=request.GET.get('cid')
    try:
        res=Course.objects.get(cno=cno)
        res.delete()
        qs=Course.objects.all()
        messages.success(request, 'deleted sucesfully')
        return render(request,'viewall_schedule.html',{'data':qs})
    except:
        qs=Course.objects.all()
        messages.success(request,'something wrong')
        return render(request,'viewall_schedule.html',{'data':qs})


def Student(request):
    return render(request,'student.html')


def student_register(request):
    return render(request,'student_register.html')


def save_student_data(request):
    name=request.POST.get('t1')
    contact=request.POST.get('t2')
    email=request.POST.get('t3')
    pwd=request.POST.get('t4')
    try:
        User.objects.create_user(name,email,pwd).save()
        res=Student_data(sname=name,contactno=contact,email=email,password=pwd)
        res.save()
        messages.success(request,'Registered sucessfully')
        return render(request,'student.html')
    except:
        messages.error(request,'try again')
        return render(request,'student.html')


def login_student(request):
    logout(request)
    return render(request,'student_login.html')

def student_login_check(request):
    user=request.POST.get('t1')
    pwd=request.POST.get('t2')
    user=authenticate(username=user,password=pwd)
    if user:
        login(request,user)
        return render(request,'welcome_student.html',{'data2':Course.objects.all()})
    else:
        messages.error(request,'invalid username and password')
        return render(request,'student_login.html')





def adminlogout(request):
    logout(request)
    return render(request,'index.html')


def welcome_student(request):
    qs=Course.objects.all()
    return render(request,'welcome_student.html')


def enroll_course(request):
    cn=request.GET.get('cname')
    sn=request.GET.get('name')
    cd=Course.objects.get(cname=cn)
    sd=Student_data.objects.get(sname=sn)
    try:
        if Enroll_data.objects.filter(sname=sd.sname,cname=cd.cname):
            messages.error(request,'this course already enrolled')
            return render(request,'welcome_student.html',{'data':Course.objects.all()})
        else:
            Enroll_data(sname=sd.sname,cname=cd.cname,phno=sd.contactno).save()
            messages.success(request,'courseenrolled sucessfully')
            return render(request,'welcome_student.html',{'data':Course.objects.all()})
    except:
        messages.error(request,'this course already enrolled')
        return render(request,'welcome_student.html',{'data':Course.objects.all()})


def student_enroll(request):
    return render(request,'welcome_student.html',{'data':Course.objects.all()})


def student_logout(request):
    logout(request)
    return render(request,'student_login.html')


def view_enroll(request):
    sn=request.GET.get('sname')
    res=Enroll_data.objects.filter(sname=sn)
    if res:
        return render(request,'welcome_student.html',{'data1':res})
    else:
        messages.error(request,'please enroll course ')
        return render(request,'welcome_student.html',{'data':Course.objects.all()})


def cencel_enroll(request):
    cn=request.GET.get('cname')
    sn=request.GET.get('sname')
    try:
        res=Enroll_data.objects.filter(cname=cn)
        res.delete()
        messages.success(request,'course cancelled')
        qs=Enroll_data.objects.filter(sname=sn)
        return render(render,'welcome_student.html',{'data1':qs})
    except:
        qs = Enroll_data.objects.filter(sname=sn)
        return render(request,'welcome_student.html',{'data1':qs})


def course_view(request):
    cn=request.GET.get('cname')
    res = Enroll_data.objects.filter(cname=cn)
    if res:
        return render(request,'python.html',{'qs':res})
    else:
        return render(request,'python.html',{'error':'no one enrolled this course'})

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
@method_decorator(csrf_exempt,name='dispatch')
def searcphone(request):
    phone=request.POST.get('phno')
    try:
        Student_data.objects.get(contactno=phone)
        res={'error':'phone no is taken'}
    except:
        res={'message':'phno is available'}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name='dispatch')
def searchemail(request):
    email=request.POST.get('email')
    try:
        Student_data.objects.get(email=email)
        res={'error':'this email is taken'}
    except:
        res={'message':'email is available'}
    return JsonResponse(res)