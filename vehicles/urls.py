from django.urls import path
from . import views


app_name = "vehicles"

urlpatterns = [
    path('', views.home, name="home"),
    path('customers/search/', views.search, name="search")
]
