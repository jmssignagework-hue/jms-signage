from django.urls import path
from .views import home, about, gallery, calculator, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('calculator/', calculator, name='calculator'),
    path('contact/', contact, name='contact'),
]
