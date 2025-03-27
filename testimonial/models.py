from django.contrib.auth import get_user_model
from django.db import models

from main.models import Product

User=get_user_model()
# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100, default='Guest')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="testimonials")
    rate = models.IntegerField(default=1)
    comment = models.TextField()

    is_new = models.BooleanField(default=True)
    is_appropriate = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.product.name} ({self.rate})"