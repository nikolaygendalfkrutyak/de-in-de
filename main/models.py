

from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models

# from account.models import Country
User=get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/categories', default='default.jpg')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __iter__(self):
        products = self.products.filter(is_visible=True)
        for product in products:
            yield product
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['sort']




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to='images/products')
    description = models.TextField(default="")

    detailed_description = models.TextField(default="")

    is_bestseller = models.BooleanField(default=False)
    rating = models.IntegerField(default=5)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    is_visible = models.BooleanField()

    sort = models.SmallIntegerField(default=0)
    class Meta:
        ordering = ['sort', 'name']

class FooterInfo(models.Model):
    #contact
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=75)
    like_info= CKEditor5Field(default='')

    #links
    like_info_more = models.TextField()
    about_us = models.TextField()
    contact_us = models.TextField()
    privacy_policy = models.TextField()
    terms_and_conditions = models.TextField()
    return_policy = models.TextField()
    faqs_and_help = models.TextField()

    #account
    account = models.TextField()
    shop_details = models.TextField()
    shopping_cart = models.TextField()
    order_history = models.TextField()

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + self.email + self.message


