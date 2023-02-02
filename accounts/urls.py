from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('login/', views.user_login, name='user_login'),
    path('<slug:slug>/', views.doctor_detail, name='doctor_detail'),
]
