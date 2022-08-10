from django.urls import resolve, reverse
from vehicles import views

from .test_vehicle_base import VechicleTestBase


class VehicleSearchViewTest(VechicleTestBase):

    def test_vehicle_search_view_function_is_correct(self):
        view = resolve(reverse('vehicles:search'))
        self.assertIs(view.func, views.search)

    def test_vehicle_search_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('vehicles:search') + '?q=teste')
        self.assertEqual(response.status_code, 200)

    def test_vehicle_search_raises_404_if_no_search_term(self):
        url = reverse('vehicles:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_vehicle_search_term_is_on_page_title_and_escaped(self):
        url = reverse('vehicles:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &lt;Teste&gt;',
            response.content.decode('utf-8')
        )

    def test_vehicle_search_can_find_customer_by_social_security_number(self):
        social_security_number_1 = '123456789'
        social_security_number_2 = '987654321'

        customer_1 = self.make_customer(**{'ssn': social_security_number_1})
        customer_2 = self.make_customer(**{'ssn': social_security_number_2})

        search_url = reverse('vehicles:search')
        response1 = self.client.get(f'{search_url}?q={social_security_number_1}')
        response2 = self.client.get(f'{search_url}?q={social_security_number_2}')

        self.assertIn(customer_1, response1.context['customer_vehicles'].keys())
        self.assertNotIn(customer_2, response1.context['customer_vehicles'].keys())

        self.assertIn(customer_2, response2.context['customer_vehicles'].keys())
        self.assertNotIn(customer_1, response2.context['customer_vehicles'].keys())

    def test_vehicle_search_can_find_customer_by_name(self):
        social_security_number_1 = '123456789'
        social_security_number_2 = '987654321'

        customer_1 = self.make_customer(**{
            'name': 'Gabriel Leal',
            'ssn': social_security_number_1
        })
        customer_2 = self.make_customer(**{
            'name': 'Gabriel Pereira',
            'ssn': social_security_number_2
        })

        response_both = self.client.get(f'{reverse("vehicles:search")}?q=Gabriel')

        self.assertIn(customer_1, response_both.context['customer_vehicles'].keys())
        self.assertIn(customer_2, response_both.context['customer_vehicles'].keys())
