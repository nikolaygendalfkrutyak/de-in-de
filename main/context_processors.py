from django.db.models import Avg
from django.db.models.functions import Coalesce

from .models import FooterInfo, Product


def footer_info(request):
    if FooterInfo.objects.exists():

        data = FooterInfo.objects.first()

        return {
            'phone' : data.phone,
            'email' : data.email,
            'address' : data.address,
            'like_info' : data.like_info,

            # links
            'like_info_more' : data.like_info_more,
            'about_us' : data.about_us,
            'contact_us': data.contact_us,
            'privacy_policy' : data.privacy_policy,
            'terms_and_conditions' : data.terms_and_conditions,
            'return_policy': data.return_policy,
            'faqs_and_help': data.faqs_and_help,

            # account
            'account': data.account,
            'shop_details' : data.shop_details,
            'shopping_cart' : data.shopping_cart,
            'order_history' : data.order_history,
        }
    else:
        return {
            'phone': '',
            'email': '',
            'address': '',
            'like_info': '',

            # links
            'like_info_more': '',
            'about_us': '',
            'contact_us': '',
            'privacy_policy': '',
            'terms_and_conditions': '',
            'return_policy': '',
            'faqs_and_help': '',

            # account
            'account': '',
            'shop_details': '',
            'shopping_cart': '',
            'order_history': '',
        }

def count_product_ratings(request):
    if Product.objects.exists():

        products = Product.objects.filter(is_visible=True).order_by('sort')
        for product in products:
            testimonials = product.testimonials.filter(is_appropriate=True)
            if testimonials.exists():
                rate = sum(testimonial.rate for testimonial in testimonials) / len(testimonials)
                product.rating = rate
                product.is_bestseller=(rate>=4)
            else:
                product.rating = 5
                product.is_bestseller=True
            product.save()
        bestseller_products = Product.objects.filter(is_visible=True, is_bestseller=True).order_by('sort')
        # Debugging: Print bestseller products in the console


        return {'products' : products, 'bestseller_products': bestseller_products}
    return {'products' : '', 'bestseller_products': ''}
