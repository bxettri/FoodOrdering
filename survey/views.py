from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
# from django.http import HttpResponse


def index(request):
    return render(request, 'survey/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            user = None
        if user is not None:
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
        return redirect('/login')
    else:
        return render(request, 'survey/login.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['rPassword']

        if password == confirm_pass:
            try:
                chk_user = User.objects.get(username=username)
            except User.DoesNotExist:
                chk_user = None

            try:
                chk_email = User.objects.get(email=email)
            except User.DoesNotExist:
                chk_email = None

            if chk_email is None:
                if chk_user is None:
                    if gender == "None":
                        messages.info(request, 'Please select your gender')
                        return redirect('/signup')

                    else:
                        user = User(full_name=fullname, dob=dob, gender=gender, email=email, username=username,
                                    password=password)
                        user.save()
                        print('User registered successfully')
                        return redirect('/')

                else:
                    messages.info(request, 'Username already exists')
                    return redirect('/signup')

            else:
                messages.info(request, 'Email already exists')
                return redirect('/signup')

        else:
            messages.info(request, 'Password not matching')
            return redirect('/signup')

    else:
        return render(request, 'survey/signup.html')
