from django.contrib import admin
from .models import Product, GalleryImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'unit', 'active')
    list_editable = ('rate', 'active')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
