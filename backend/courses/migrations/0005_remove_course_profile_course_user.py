# Generated by Django 4.1.2 on 2022-11-07 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_remove_course_subject_course_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='profile',
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
