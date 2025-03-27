from django.urls import path

from manager.views import order_accepting, testimonial_check, testimonials_management, orders_management, \
    contacts_management

app_name = 'manager'

urlpatterns= [
    path('orders/', orders_management, name='orders'),
    path('order_accept/<int:pk>/<str:action>', order_accepting, name='order_accept'),
    path('testimonials', testimonials_management, name='testimonials'),
    path('testimonial_check/<int:pk>/<str:action>', testimonial_check, name='testimonial_check'),

    path('contacts', contacts_management, name='contacts'),
]