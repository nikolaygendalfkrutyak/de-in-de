"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import request

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import UserLoginView, UserRegistrationView, logout_view, UserProfileUpdateView
from main.views import not_home, home, change_product, checkout_order, shop_detail, submit_review, contact_form
from testimonial.views import testimonials_view

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('sign_in/', UserLoginView.as_view(), name='sign_in'),

    path('sign_up/',UserRegistrationView.as_view(), name = 'sign_up'),
    path('logout', logout_view, name='logout'),
    path('account_settings', UserProfileUpdateView.as_view(), name='account_settings'),
    path('change_product/<int:product_id>/<str:operation>', change_product, name='change_product'),
    path('<str:template_name>/', not_home, name='not_home'),
    path('checkout_order', checkout_order, name='checkout_order'),
    path('manager/', include('manager.urls', namespace='manager')),
    path('shop_detail/<int:pk>', shop_detail, name='shop_detail'),
    path('testimonials/', testimonials_view, name='testimonials'),
    path('submit_review/<int:pk>', submit_review, name='submit_review'),
    path('contact_form', contact_form, name='contact_form')
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
