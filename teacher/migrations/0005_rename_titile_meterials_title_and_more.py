# Generated by Django 5.0.1 on 2024-02-17 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_meterials_videostudylink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meterials',
            old_name='Titile',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='videostudylink',
            old_name='Titile',
            new_name='Title',
        ),
    ]