# Generated by Django 4.2 on 2023-04-16 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_text_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='users',
        ),
    ]
