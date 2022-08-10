from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from .test_vehicle_base import VechicleTestBase


class CustomerModelTest(VechicleTestBase):

    def setUp(self):
        self.customer = self.make_customer()
        return super().setUp()

    def test_customer_name_field_max_length(self):
        self.customer.name = ''.rjust(66, 'A')
        with self.assertRaises(ValidationError):
            self.customer.full_clean()

    def test_customer_name_field_is_blank(self):
        self.customer.name = ''
        with self.assertRaises(ValidationError):
            self.customer.full_clean()

    def test_customer_social_security_number_is_blank(self):
        self.customer.social_security_number = ''
        with self.assertRaises(ValidationError):
            self.customer.full_clean()

    def test_customer_social_security_number_with_duplicate_values(self):
        with self.assertRaises(IntegrityError):
            self.customer_duplicate_ssn = self.make_customer(ssn='123456789')
