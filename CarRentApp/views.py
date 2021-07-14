from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CarCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

# from .service import add_car
# Create your views here.


def home(request):
    form = CarCreationForm()
    if request.method == 'POST':
        form = CarCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'pages/home.html', {'form': form})

def car_update_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarCreationForm(instance = car)
    if request.method == 'POST':
        form = CarCreationForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_change', pk=pk)
    return render(request, 'pages/home.html', {'form': form})

def load_cars(request):
    brand_id = request.GET.get('brand_id')
    model = CarModel.objects.filter(brand_id=brand_id)
    return render(request, 'pages/car_dropdown_options.html', {'model': model})

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
