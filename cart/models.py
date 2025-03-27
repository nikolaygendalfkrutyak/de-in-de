from django.contrib.auth import get_user_model
from django.db import models

from account.models import CustomUser, ShippingDetails
from main.models import Product

User = get_user_model()
# Create your models here.

class ChosenProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chosen_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="chosen_products")
    amount = models.IntegerField(default=1)
    def price(self):
        price = self.amount * self.product.price
        return price
    def __str__(self):
        return f"{self.product.name} ({self.amount})"


    @staticmethod
    def get_cart_count(user):
        amount_of_all=0
        for chosen_product in ChosenProduct.objects.filter(user=user):
            amount_of_all+=chosen_product.amount
        return amount_of_all

class OrderedProduct(models.Model):
    order = models.ForeignKey("Orders", on_delete=models.CASCADE, related_name="ordered_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)
    def price(self):
        return self.amount * self.price_at_order

    def __str__(self):
        return f"{self.product.name} ({self.amount})"

class Orders(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shipping_details = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE)
    ordered_products = models.ManyToManyField(OrderedProduct)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    def price(self):
        total =3
        for ordered_product in OrderedProduct.objects.filter(order=self):
            total += ordered_product.price()
        return total
    def __str__(self):
        return f"Order {self.pk} - {self.user.username}"

    def get_ordered_products(self):
        return OrderedProduct.objects.filter(order=self)
