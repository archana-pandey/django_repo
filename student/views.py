from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'regform.html')

# For Testing
def studentRegistration(request):
    name = request.POST.get('name', '')
    fname = request.POST.get('fname', '')
    mname = request.POST.get('mname','')
    dob = request.POST.get('dob','')
    res = {'name':name, 'fname':fname,'mname':mname,'dob':dob}
    return render(request,'result.html',{'result':res})
    