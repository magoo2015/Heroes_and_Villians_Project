# Generated by Django 4.0.5 on 2022-06-24 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0002_rename_catchphrass_super_catchphrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.super_type'),
        ),
    ]
