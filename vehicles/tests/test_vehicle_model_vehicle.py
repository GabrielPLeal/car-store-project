from django.core.exceptions import ValidationError

from .test_vehicle_base import VechicleTestBase


class CustomerModelTest(VechicleTestBase):

    def setUp(self):
        self.vehicle = self.make_vehicle()
        return super().setUp()

    def test_vehicle_model_field_is_different_the_choices(self):
        self.vehicle.model = 4
        with self.assertRaises(ValidationError):
            self.vehicle.full_clean()

    def test_vehicle_color_field_is_different_the_choices(self):
        self.vehicle.model = 4
        with self.assertRaises(ValidationError):
            self.vehicle.full_clean()

    def test_vehicle_customer_reached_max_num_of_vehicles(self):
        customer = self.make_customer(name='Customer 2', ssn='456789123')
        for num_vehicles in range(3):
            self.vehicle = self.make_vehicle(customer_data={'id': customer.id})
        with self.assertRaises(ValidationError):
            self.vehicle.clean()


