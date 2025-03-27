from django.contrib import admin

from cart.models import  ChosenProduct, Orders


admin.site.register(ChosenProduct)
admin.site.register(Orders)
