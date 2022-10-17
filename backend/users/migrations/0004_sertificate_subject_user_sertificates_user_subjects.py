# Generated by Django 4.1.2 on 2022-10-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_picture_rename_test_testunit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=32)),
                ('document', models.CharField(max_length=64)),
                ('is_verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='sertificates',
            field=models.ManyToManyField(blank=True, to='users.sertificate'),
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='users.subject'),
        ),
    ]