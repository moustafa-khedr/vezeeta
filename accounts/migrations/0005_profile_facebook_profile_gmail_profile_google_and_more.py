# Generated by Django 4.1.6 on 2023-02-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_address_profile_address_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gmail',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='google',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
