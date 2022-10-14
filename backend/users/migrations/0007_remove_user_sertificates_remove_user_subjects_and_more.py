# Generated by Django 4.1.2 on 2022-10-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_document_sertificate_document_path_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sertificates',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subjects',
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.ManyToManyField(to='users.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serctificates', models.ManyToManyField(to='users.sertificate')),
            ],
        ),
    ]
