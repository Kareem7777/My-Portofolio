from django.urls import path
from core import views

# Create your urls here.

urlpatterns = [
    path('', views.home, name='home_url'),
    path('contact', views.contact, name='contact_url'),
]