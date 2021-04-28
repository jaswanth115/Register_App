from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here. 


def home(request):
    student=Student.objects.all()
    content={'student':student}

    return render(request, 'home.html', content)

def register(request):
    if request.method=='POST':
        student=Student()
        usn=request.POST.get('usn')
        name=request.POST.get('name')
        student.usn=usn
        student.name=name
        student.save()
        return redirect('home')

    return render(request, 'register.html')