# Generated by Django 4.1 on 2022-08-09 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='person',
            new_name='customer',
        ),
    ]
