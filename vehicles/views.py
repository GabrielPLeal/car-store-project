from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from .models import Customer, Vehicle


def home(request):
    customers = Customer.objects.all()
    customer_vehicles = organized_customers_data(customers)
    return render(request, 'vehicles/pages/home.html', context={
        'customer_vehicles': customer_vehicles
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    customers = Customer.objects.filter(
        Q(name__icontains=search_term) |
        Q(social_security_number=search_term)
    ).order_by('-id')

    customer_vehicles = organized_customers_data(customers)

    return render(request, 'vehicles/pages/search.html', context={
        'customer_vehicles': customer_vehicles,
        'page_title': f'Search for {search_term}',
        'search_term': search_term
    })


def organized_customers_data(customers):
    customer_vehicles = {}
    for customer in customers:
        vehicles = Vehicle.objects.filter(customer_id=customer.id)
        customer_vehicles.setdefault(customer, vehicles)
    return customer_vehicles