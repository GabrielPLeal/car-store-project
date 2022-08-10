from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=65, blank=False, null=False)
    social_security_number = models.CharField(max_length=9, unique='True', blank=False, null=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    MODELS_CHOICES = (
        (1, 'Hatch'),
        (2, 'Sedan'),
        (3, 'Convertible')
    )

    COLORS_CHOICES = (
        (1, 'Yellow'),
        (2, 'Blue'),
        (3, 'Gray')
    )

    model = models.IntegerField(choices=MODELS_CHOICES)
    color = models.IntegerField(choices=COLORS_CHOICES)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,

    )

    def clean(self):
        from django.core.exceptions import ValidationError

        vehicles = Vehicle.objects.filter(customer_id=self.customer.id)
        quantity_customer_vehicles = len(vehicles)
        max_quantity_vehicles = 3

        if quantity_customer_vehicles == max_quantity_vehicles:
            raise ValidationError('Customer reached the maximum number of vehicles.')

    def __str__(self):
        return f'{self.id}'
