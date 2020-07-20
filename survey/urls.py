from django.urls import path
from . import views
from .views import *

app_name = 'survey'
urlpatterns = [
    path("", IndexView.as_view()),  # OR path('', views.index, name='index'),
    path("signup/", SignupView.as_view()),
]
