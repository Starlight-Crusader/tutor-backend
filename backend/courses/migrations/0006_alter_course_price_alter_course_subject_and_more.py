# Generated by Django 4.1.2 on 2022-11-07 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_alter_subject_subject_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_remove_course_profile_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(choices=[(1, 'ONLINE'), (2, 'OFFLINE')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
