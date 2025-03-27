from account.models import ShippingDetails
from cart.models import ChosenProduct, Orders, OrderedProduct


def create_order(user):
    chosen_products = ChosenProduct.objects.filter(user=user)

    if not chosen_products.exists():
        return None

    shipping = ShippingDetails.objects.create(
        first_name=user.first_name,
        last_name=user.last_name,
        mobile_number=user.mobile_number,
        postcode=user.postcode,
        country=user.country,
        town=user.town,
        street_and_house=user.street_and_house,
    )

    order = Orders.objects.create(user=user, shipping_details=shipping)

    for chosen in chosen_products:
        ordered_product = OrderedProduct.objects.create(
            order=order,
            product=chosen.product,
            amount=chosen.amount,
            price_at_order=chosen.product.price
        )
        order.ordered_products.add(ordered_product)

    chosen_products.delete()

    return order