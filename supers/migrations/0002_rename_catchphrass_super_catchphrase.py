# Generated by Django 4.0.5 on 2022-06-24 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='catchphrass',
            new_name='catchphrase',
        ),
    ]
