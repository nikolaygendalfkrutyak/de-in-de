from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import ReviewForm
from main.models import Product
from testimonial.models import Testimonial


# Create your views here.
def testimonials_view(request):
    testimonials = Testimonial.objects.filter(is_appropriate=True)
    context = {
        'testimonials': testimonials
    }
    return render(request, 'testimonial.html', context)

