# Generated by Django 4.1.2 on 2022-10-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='document_path',
            field=models.FileField(upload_to='docs/certificates'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='subject_name',
            field=models.CharField(max_length=100),
        ),
    ]
