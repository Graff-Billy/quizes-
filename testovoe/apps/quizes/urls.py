from django.urls import path 
from . import views

app_name = 'quizes'
urlpatterns = [

    path('', views.index, name='index'),
    path('quizes/', views.list, name ='list'),
    path('current_user/', views.current_user, name ='current_user'),
    path('<int:quiz_id>/', views.detail, name ='detail'),
]