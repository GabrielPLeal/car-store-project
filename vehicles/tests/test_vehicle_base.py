from django.test import TestCase
from vehicles.models import Customer, Vehicle


class VechicleTestBase(TestCase):

    def setUp(self):
        return super().setUp()

    def make_customer(self, name='Customer 1', ssn='123456789', age=20):
        return Customer.objects.create(
            name=name,
            social_security_number=ssn,
            age=age
        )

    def make_vehicle(self, model=1, color=1, customer_data=None):

        if customer_data is None:
            customer = self.make_customer()
        else:
            customer = Customer.objects.get(**customer_data)

        return Vehicle.objects.create(
            model=model,
            color=color,
            customer=customer
        )
