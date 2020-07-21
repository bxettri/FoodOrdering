from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
# from django.http import HttpResponse


def index(request):
    return render(request, 'survey/index.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPass = request.POST['confirmPassword']

        if password == confirmPass:
            if User.objects.filter(username__exists=username):
                messages.info(request, 'Username already exists')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('/signup')
            else:
                user = User(full_name=fullname, dob=dob, gender=gender, email=email, username=username, password=password)
                user.save();
                print('User registered successfully')
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/signup')

    return render(request, 'survey/signup.html')


