from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required

# from .service import add_car
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')


@login_required(login_url='login')
def addPost(request):
    form = CarCreationForm()
    form1 = PostCreationForm()
    if request.method == 'POST':
        item = Car(added_by = request.user)
        form = CarCreationForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            new_car = form.save()
            car = CarPost(car = new_car, added_by = request.user)
            form1 = PostCreationForm(request.POST, request.FILES, instance=car)
            if form1.is_valid():
                form1.save()
    return render(request, 'pages/create_post.html', {'form': form,
                                               'form1': form1})



# def car_update_view(request, pk):
#     car = get_object_or_404(Car, pk=pk)
#     form = CarCreationForm(instance = car)
#     if request.method == 'POST':
#         form = CarCreationForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             return redirect('car_change', pk=pk)
#     return render(request, 'pages/create_post.html', {'form': form})

def load_cars(request):
    brand_id = request.GET.get('brand_id')
    model = CarModel.objects.filter(brand_id=brand_id)
    return render(request, 'pages/car_dropdown_options.html', {'model': model})

def catalogue(request):
    data = CarPost.objects.all()
    return render(request, 'pages/catalogue.html', {'data':data})

def posts(request, pk):
    data = CarPost.objects.get(pk = pk)
    return render(request, 'pages/posts.html', {'data':data})

def order(request, pk):
    form = OrderForm()
    if request.method == "POST":
        post_id = CarPost.objects.get(pk = pk)
        order = Order(chosen_car = post_id )
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    return render(request, 'pages/order.html', {'form': form})
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
    return redirect('home')
