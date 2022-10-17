# Generated by Django 4.1.2 on 2022-10-17 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
        ('certificates', '0001_initial'),
        ('users', '0018_remove_testmanytomany_test_record_and_more'),
        ('profiles', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='reviews.review'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sertificates',
            field=models.ManyToManyField(blank=True, to='certificates.certificate'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='subjects.subject'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]