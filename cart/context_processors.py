from .models import ChosenProduct, OrderedProduct, Orders


def cart_context(request):
    if request.user.is_authenticated:
        user = request.user
        chosen_products = ChosenProduct.objects.filter(user=user)
        orders = Orders.objects.filter(user=user)
        cart_count = ChosenProduct.get_cart_count(user=user)
        shipping_price=3
        def subtotal():
            price = sum(chosen_product.price() for chosen_product in chosen_products)
            return price

        def total():
            return subtotal() + shipping_price
    else:
        subtotal =0
        total =0
        shipping_price = 0
        chosen_products = []
        orders = []
        cart_count = 0

    return {
        'orders': orders,
        'chosen_products': chosen_products,
        'cart_count': cart_count,
        'subtotal': subtotal,
        'total': total,
        'shipping_price': shipping_price,
    }