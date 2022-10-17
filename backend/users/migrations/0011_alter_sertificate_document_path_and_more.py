# Generated by Django 4.1.2 on 2022-10-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sertificate',
            name='document_path',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='sertificate',
            name='subject_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='testunit',
            name='test_data',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=32),
        ),
    ]