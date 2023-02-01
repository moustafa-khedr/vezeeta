from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField('name :', max_length=50)
    who_i = models.TextField('who_am_I :', max_length=250)
    price = models.IntegerField('Examination price :')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name
