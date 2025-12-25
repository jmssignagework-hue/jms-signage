from django.shortcuts import render
from .models import GalleryImage, Product

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def calculator(request):
    products = Product.objects.filter(active=True)
    return render(request, 'calculator.html', {'products': products})
def contact(request):
    return render(request, 'contact.html')
