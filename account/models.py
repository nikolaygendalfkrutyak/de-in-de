from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

#
# class Country(models.Model):
#     And I didn't make it... alive

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=15)
    postcode=models.CharField(max_length=10)
    country=models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    street_and_house=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ShippingDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    street_and_house = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.last_name}, {self.user_email}, {self.mobile_number}, {self.postcode}, {self.country}, {self.town}, {self.street_and_house}"




