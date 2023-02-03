from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Login_Form, UpdateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

@login_required()
def my_profile(request):

    return render(request, 'registration/my_profile.html', {
    })


def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            print('done save')
            return redirect('accounts:doctors_list')
        else:
            user_form = UpdateUserForm(instance=request.user)
            print('not valid')

    return render(request, 'registration/update_profile.html', {
        'user_form':user_form
    })