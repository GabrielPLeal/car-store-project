# Generated by Django 4.1 on 2022-08-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_customer_sales_oportunity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='sales_oportunity',
            new_name='is_sales_oportunity',
        ),
    ]
