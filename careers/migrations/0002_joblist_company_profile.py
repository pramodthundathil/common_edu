# Generated by Django 5.0.1 on 2024-02-12 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='company_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.recruiterdata'),
        ),
    ]
