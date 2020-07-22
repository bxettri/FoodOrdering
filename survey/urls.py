from django.urls import path
from . import views
from .views import *

app_name = 'survey'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
