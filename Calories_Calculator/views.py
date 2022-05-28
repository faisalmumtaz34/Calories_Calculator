from django.shortcuts import render,redirect
from . form import UserForm, CreateUserForm, AddFood
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('add_details')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_details')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                
        return render(request, 'Calories_Calculator/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('add_details')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Was Created For '+user)
                return redirect(login)
        context = {'form':form}
        return render(request, 'Calories_Calculator/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_details(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Calories_Calculator/user_details.html', context)

@login_required(login_url='login')
def add_food(request):
    form = AddFood()
    if request.method == 'POST':
        form = AddFood(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Calories_Calculator/add_food.html', context)
