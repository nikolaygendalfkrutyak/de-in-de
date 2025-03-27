from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from cart.models import Orders
from main.models import ContactMessage
from testimonial.models import Testimonial


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='manager').exists() or user.is_superuser

@login_required(login_url='sign_in')
@user_passes_test(is_manager)
def orders_management(request):
    data = Orders.objects.filter(accepted=False).order_by('created_at')
    pro_data = Orders.objects.filter(accepted=True).order_by('created_at')

    context = {'unaccepted_orders': data, 'accepted_orders': pro_data}
    return render(request, 'orders_management.html', context)

@login_required(login_url='sign_in')
@user_passes_test(is_manager)
def testimonials_management(request):
    data = Testimonial.objects.filter(is_new=True)
    context = {'unchecked_testimonials': data}
    return render(request, 'testimonials_management.html', context)

@login_required(login_url='sign_in')
@user_passes_test(is_manager)
def contacts_management(request):
    data = ContactMessage.objects.all()
    context = {'contact_messages': data}
    return render(request, 'contacts_management.html', context)

@login_required(login_url='sign_in')
@user_passes_test(is_manager)
def order_accepting(request, pk, action):
    data = Orders.objects.get(pk=pk)
    if action == 'accept':
        data.is_accepted= True
    if action == 'reject':
        data.is_accepted = False
    data.save()
    return redirect('manager:orders')

@login_required(login_url='sign_in')
@user_passes_test(is_manager)
def testimonial_check(request, pk, action):
    data = Testimonial.objects.get(pk=pk)
    if action == 'accept':
        data.is_appropriate = True
    if action == 'decline':
        data.is_appropriate = False
    data.save()
    return redirect('manager:testimonials')