# Generated by Django 4.1.2 on 2022-10-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.IntegerField(blank=True, choices=[(1, 'TUTOR'), (2, 'STUDENT')]),
        ),
    ]