from django.urls import resolve, reverse
from vehicles import views

from .test_vehicle_base import VechicleTestBase


class VehicleHomeViewTest(VechicleTestBase):

    def test_vehicle_home_view_function_is_correct(self):
        view = resolve(reverse('vehicles:home'))
        self.assertIs(view.func, views.home)

    def test_vehicle_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('vehicles:home'))
        self.assertEqual(response.status_code, 200)

    def test_vehicle_home_view_loads_correct_template(self):
        response = self.client.get(reverse('vehicles:home'))
        self.assertTemplateUsed(response, 'vehicles/pages/home.html')

    def test_vehicle_home_template_shows_no_customers_found_if_no_customer(self):
        response = self.client.get(reverse('vehicles:home'))
        self.assertIn(
            '<h1>No costumers found here!</h1>',
            response.content.decode('utf-8')
        )

    def test_vehicle_home_template_loads_costumer_has_no_cars_and_is_sales_opportunity(self):
        self.make_customer()

        response = self.client.get(reverse('vehicles:home'))
        content = response.content.decode('utf-8')
        response_context_customers = response.context['customer_vehicles'].keys()

        self.assertIn('Customer 1', content)
        self.assertIn('SALES OPPORTUNITY!', content)
        self.assertIn('The costumer has no cars!', content)
        self.assertEqual(len(response_context_customers), 1)

    def test_vehicle_home_template_loads_costumer_has_cars(self):
        self.make_vehicle()

        response = self.client.get(reverse('vehicles:home'))
        content = response.content.decode('utf-8')
        response_context_customers = response.context['customer_vehicles'].keys()

        self.assertIn('Customer 1', content)
        self.assertIn('COLOR: Yellow', content)
        self.assertEqual(len(response_context_customers), 1)
