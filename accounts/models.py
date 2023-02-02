from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

TYPE_OF_PERSON = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Profile(models.Model):

    DOCTOR_IN = (
        ("Dermatologist", "Dermatologist"),
        ("dentist", "dentist"),
        ("psychiatrist", "psychiatrist"),
        ("newborn pediatrician", "newborn pediatrician"),
        ("neurologist", "neurologist"),
        ("orthopedist", "orthopedist"),
        ("obstetrician-gynecologist", "obstetrician-gynecologist"),
        ("ear, nose and throat doctor", "ear, nose and throat doctor"),
        ("cardiologist and vascular doctor", "cardiologist and vascular doctor"),
        ("hematologist", "hematologist"),
        ("oncologist", "oncologist"),
        ("internal doctor", "internal doctor"),
        ("Dietitian and Nutritionist", "Dietitian and Nutritionist"),
        ("pediatric surgeon", "pediatric surgeon"),
        ("surgical oncologist", "surgical oncologist"),
        ("vascular surgeon", "vascular surgeon"),
        ("Plastic Surgeon Doctor", "Plastic Surgeon Doctor"),
        ("Obesity and Laparoscopic Surgeon", "Obesity and Laparoscopic Surgeon"),
    )


    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField('name :', max_length=50)
    subtitle = models.CharField(max_length=80)
    address = models.CharField('Governorate', max_length=50)
    address_detail = models.CharField('Detailed address', max_length=50)
    number_phone = models.CharField(max_length=50)
    working_hours = models.CharField(max_length=50)
    waiting_time = models.IntegerField(blank=True, null=True)
    who_i = models.TextField('who_am_I :', max_length=250)
    price = models.IntegerField('Examination price :', blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    google = models.CharField(max_length=150, blank=True, null=True)
    gmail = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField('Personal Image', upload_to='profile', blank=True, null=True)
    join_us = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    type_of_person = models.CharField('gender', choices=TYPE_OF_PERSON, max_length=50, blank=True, null=True)
    specialist_doctor = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField('slug', blank=True, null=True)
    doctor = models.CharField('doctor ?', choices=DOCTOR_IN, max_length=80, blank=True, null=True)




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '%s' % self.user.username  # appearance with username (%s) to number in username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
