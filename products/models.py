from django.db import models

class Product(models.Model):
    UNIT_CHOICES = [
        ('inch', 'Per Inch'),
        ('sq_inch', 'Per Square Inch'),
        ('sq_ft', 'Per Square Foot'),
    ]

    name = models.CharField(max_length=100)
    rate = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Gallery Image"
