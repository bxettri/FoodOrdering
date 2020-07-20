from django.shortcuts import render
from django.views.generic import *


# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return render(request, 'survey/index.html')
#
#
# def signup(request):
#     return render(request, 'survey/signup.html')


class IndexView(TemplateView):
    template_name = "survey/index.html"


class SignupView(TemplateView):
    template_name = "survey/signup.html"
