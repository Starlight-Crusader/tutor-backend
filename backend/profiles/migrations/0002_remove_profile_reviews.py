# Generated by Django 4.1.2 on 2022-11-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reviews',
        ),
    ]