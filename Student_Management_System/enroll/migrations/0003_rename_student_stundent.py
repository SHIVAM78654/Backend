# Generated by Django 4.2.11 on 2024-05-08 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_rename_stundent_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Stundent',
        ),
    ]
