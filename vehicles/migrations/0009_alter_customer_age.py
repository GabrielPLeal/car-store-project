# Generated by Django 4.1 on 2022-08-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_remove_customer_is_sales_oportunity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]