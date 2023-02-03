from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('update_profile/', views.update_profile, name= 'update_profile'),
    path('<slug:slug>/', views.doctor_detail, name='doctor_detail'),
]
