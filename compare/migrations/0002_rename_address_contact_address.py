# Generated by Django 3.2.5 on 2022-01-07 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Address',
            new_name='address',
        ),
    ]
