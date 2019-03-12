from django.urls import path, include
from . import views
from .views import ContactUs

urlpatterns = [

    path('', views.home),
    path('contact/', ContactUs.as_view(), name='contact'),
]
