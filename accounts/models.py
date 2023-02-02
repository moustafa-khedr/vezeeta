from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField('name :', max_length=50)
    who_i = models.TextField('who_am_I :', max_length=250)
    price = models.IntegerField('Examination price :', blank=True, null=True)
    image = models.ImageField('Personal Image', upload_to='profile')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '%s' % self.user.username  # appearance with username (%s) to number in username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
