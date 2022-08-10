from django.test import TestCase
from django.urls import reverse


class VehicleUrlsTest(TestCase):

    def test_vehicle_home_url_is_correct(self):
        url = reverse('vehicles:home')
        self.assertEqual(url, '/')

    def test_vehicle_search_url_is_correct(self):
        url = reverse('vehicles:search')
        self.assertEqual(url, '/customers/search/')
