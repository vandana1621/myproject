from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.db import connection
from django.urls import reverse
from django.contrib import messages

from myapp.models import Subcategory


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect(reverse('myapp:index'))

        else:
            # User could not be authenticated, show an error message
            messages.error(request, 'Invalid username or password, Please try again.')

    return render(request, 'myapp/page-login.html')


def index(request):
    context = {}  # Define the context dictionary
    if request.user.is_authenticated:
        context['user'] = request.user
    return render(request, 'myapp/index.html', context)
    # return redirect(reverse('myapp:index'))  # Uncomment this line if needed


def user_logout(request):
    # Redirect to the login page
    logout(request)
    return redirect(reverse('myapp:login'))


def SubcategoryMaster(request):
    '''subcategory = Subcategory.objects.get(pk=subcategory_id)'''
    return render(request, 'myapp/performance.html')


def EquipmentMaster(request):
    return render(request, 'myapp/performance1.html')


def Orders_Summary(request):
    return render(request, 'myapp/task.html')


def User_master(request):
    return render(request, 'myapp/employee.html')


def connects(request):
    return render(request, 'myapp/contacts.html')


def Calendar(request):
    return render(request, 'myapp/app-calender.html')

def reports(request):
    return render(request, 'myapp/reports.html')

