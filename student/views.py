from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
def home(request):
    return render(request,'homepage.html')
    
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        fname = request.POST.get('fname', '')
        mname = request.POST.get('mname','')
        dob = request.POST.get('dob','')
        student = Student(name=name, fname=fname, mname=mname, dob=dob)
        student.save()
        res = {'name':name, 'fname':fname,'mname':mname,'dob':dob}

    return render(request,'regform.html')

# For Testing
def studentRegistration(request):
    name = request.POST.get('name', '')
    fname = request.POST.get('fname', '')
    mname = request.POST.get('mname','')
    dob = request.POST.get('dob','')
    student = Student(name=name, fname=fname, mname=mname, dob=dob)
    student.save()
    res = {'name':name, 'fname':fname,'mname':mname,'dob':dob}
    return render(request,'regform.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
    