# Generated by Django 4.1.2 on 2022-10-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_rename_text_rewiew_rewiew_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=64),
        ),
    ]