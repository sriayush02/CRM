from django.shortcuts import render, redirect
#from django.http import HttpResponse
from . models import Record
#from django import forms
from .forms import CreateUserForm, LoginForm,  UpdateRecordForm ,CreateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# homepage
def home(request):
    return render(request, 'crudapp/index.html')

#Register a new user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account created Succsessfully !")
            return redirect("my-login")
        
    context ={'form' : form}
    return render(request,'crudapp/register.html',context=context)

#login user
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                auth.login(request , user)
                return redirect("dashboard")
            
    context={'form':form}
    return render(request,'crudapp/my-login.html',context=context)

#dashboard
@login_required(login_url='my-login')
def dashboard(request):

    my_records =Record.objects.all()

    context = {'records' : my_records}

    return render(request, 'crudapp/dashboard.html', context = context)

# Create record
@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method =="POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record has created !")
            return redirect("dashboard")
        
    context ={'form' :form}
    return redirect(request, 'crudapp/create-record.html', context = context)

# Update record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id = pk)
    form = UpdateRecordForm(instance=record)
    if request.method =="POST":
        form = UpdateRecordForm(request.POST, instance= record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record has been updated !")
            return redirect("dashboard")
        
    context ={'form':form}
    return render(request,'crudapp/update-record.html',context = context)

#Read record
@login_required(login_url='my-login')
def read_record(request,pk):
    all_records = Record.objects.get(id=pk)
    context = {'record':all_records}
    return render(request, 'crudapp/view-record.html', context = context)

# Delete Record
@login_required(login_url='my-login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record has been deleted !")
    return redirect("dashboard")

# Logout
def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout Successfully !")
    return redirect("my-login")









# Create your views here.
