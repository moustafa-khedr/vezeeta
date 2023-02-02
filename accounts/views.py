from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Login_Form
from django.contrib.auth import authenticate, login


# Create your views here.
def doctors_list(request):
    doctors = User.objects.all()

    return render(request, 'registration/doctors_list.html', {
        'doctors': doctors,
    })


def doctor_detail(request, slug):
    doctor_detail = Profile.objects.get(slug=slug)

    return render(request, 'registration/doctor_detail.html', {
        'doctor_detail': doctor_detail,
    })


def user_login(request):
    if request.method == "POST":
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctors_list',)
    else:
        form = Login_Form()
    return render(request, 'registration/login.html', {'form': form})
