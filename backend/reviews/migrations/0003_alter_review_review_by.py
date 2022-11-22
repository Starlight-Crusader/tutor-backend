# Generated by Django 4.1.2 on 2022-11-20 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('reviews', '0002_alter_review_review_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_authors', to='profiles.profile'),
        ),
    ]