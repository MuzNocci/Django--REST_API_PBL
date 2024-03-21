from django.urls import path
from rest_api import views



urlpatterns = [

    path('', views.get_users, name='get_users'),
    path('user/<str:nick>', views.get_user, name='get_user'),
    path('data/', views.user_manager, name='data_user')
    
]
