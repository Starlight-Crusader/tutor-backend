# Generated by Django 4.1.2 on 2022-11-09 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_rename_is_staff_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
