# Generated by Django 5.0.1 on 2024-02-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_studentprofile_photo_studentprofile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='Phone_number',
            field=models.IntegerField(),
        ),
    ]