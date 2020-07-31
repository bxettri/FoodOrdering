from django.urls import path
from . import views
app_name = 'survey'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('yourSurvey/', views.your_survey, name='your_survey'),


]
