from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


from cart.services import create_order
from testimonial.models import Testimonial
from .forms import ReviewForm, ContactForm
from .models import  Category, Product
from cart.models import ChosenProduct


ALLOWED_TEMPLATES = ['', "cart", "testimonial", "shop","checkout", "contact", "order_success", "orders", 'add_testimonial']
# Create your views here.
def home(request):
    categories = Category.objects.filter(is_visible=True).order_by('sort')
    testimonials = Testimonial.objects.filter(is_appropriate=True)

    context = {'categories': categories, 'testimonials':testimonials}
    return render(request,  "main.html", context=context)

def not_home(request, template_name):
    if template_name not in ALLOWED_TEMPLATES:
        return render(request, "404.html", status=404)  # 404 otherwise
    user = request.user
    categories = Category.objects.filter(is_visible=True).order_by('sort')
    testimonials = Testimonial.objects.filter(is_appropriate=True)
    form = ContactForm()

    context = {'user':user,'categories': categories, 'form':form,
               'testimonials': testimonials}
    return render(request, template_name+".html", context=context)



@login_required
def change_product(request, product_id, operation):
    if operation == "add":
        product = get_object_or_404(Product, id=product_id)
        chosen_product, created = ChosenProduct.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'amount': 1}
        )

        if not created:
            chosen_product.amount += 1
            chosen_product.save()

        return redirect('not_home', 'cart')
    if operation == "decrease":
        chosen_product = get_object_or_404(ChosenProduct, id=product_id, user=request.user)

        if chosen_product.amount > 1:
            chosen_product.amount -= 1
            chosen_product.save()
        else:
            chosen_product.delete()  # Remove item if 0

        # Copied this JSON stuff from some example... Not sure how it works but anyway...
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"success": True, "new_amount": chosen_product.amount if chosen_product.amount > 0 else 0})

        return redirect('not_home', 'cart')
    if operation == "delete":
        chosen_product = get_object_or_404(ChosenProduct, id=product_id, user=request.user)
        chosen_product.delete()
        return redirect('not_home', 'cart')

def product_list(request):
    categories = Category.objects.all()
    products_by_category = {category: Product.objects.filter(category=category) for category in categories}

    all_products = Product.objects.all()
    products_by_category["All"] = all_products  # Adding "All" category

    context = {
        "categories": categories,
        "products_by_category": products_by_category,
    }
    return render(request, "main.html", context)

def checkout_order(request):
    order = create_order(request.user)
    if order:
        return redirect("not_home", 'order_success')
    return redirect("cart")

def shop_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    related_products = Product.objects.filter(category=product.category)
    testimonials = product.testimonials.filter(is_appropriate=True)
    review_form = ReviewForm()
    context={
        "product": product,
        "related_products": related_products,
        "review_form": review_form,
        'testimonials': testimonials
    }

    return render(request, "shop-detail.html", context)

def submit_review(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.product = product
            testimonial.save()
            return redirect('shop_detail', pk=pk)

    else:
        form = ReviewForm()

    return render(request, 'shop-detail.html', {'form': form, 'product': product})

def contact_form(request):

    if request.method=="POST":
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            contact_message = c_form.save()
            contact_message.save()
            return redirect('not_home', 'contact')
    else:
        c_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': c_form})

