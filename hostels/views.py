from django.shortcuts import redirect
from django.shortcuts import render
from .models import Employee
from .forms import Employeeform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def hostel(request):
    emps=Employee.objects.all()
    return render(request,'hostels/index.html',{'employee':emps})

@login_required
def employee(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'hostels/details.html',{'employee':employee})

@login_required
def new(request):
    if request.POST:
        form=Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hostels/')
    form=Employeeform()
    return render(request,'hostels/new.html',{'form':form})

@login_required
def update(request,id):
    employee=Employee.objects.get(id=id)
    form=Employeeform(instance=employee)
    if request.POST:
        form=Employeeform(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect(f'/hostels/{id}/')
    return render(request,'hostels/update.html',{'form':form})

@login_required
def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/hostels/')

def sign_up(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    form=UserCreationForm()
    return render(request,'registration/sign_up.html',{'form':form})
