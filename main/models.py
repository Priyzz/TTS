import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0) 
    brand = models.CharField(max_length=100, blank=True)  
    size = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    
    def is_in_stock(self):
        """Cek apakah produk masih tersedia."""
        return self.stock > 0

    def short_description(self, length=50):
        """Ringkasan deskripsi produk."""
        return (self.description[:length] + '...') if len(self.description) > length else self.description