from .models import Profile
from django.shortcuts import render
from django.contrib.auth.models import User


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