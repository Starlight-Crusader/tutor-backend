# Generated by Django 4.1.2 on 2022-11-05 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_alter_subject_subject_name'),
        ('courses', '0003_remove_course_subjects_course_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
        ),
    ]