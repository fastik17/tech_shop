from datetime import date

from celery.app import task
from dateutil.relativedelta import relativedelta
from products.models import Product
from products.constants import DISCOUNT


@task
def make_product_discount():
    one_month_ago = date.today() - relativedelta(month=1)

    products_to_discount = Product.objects.get(created_at=one_month_ago)
    if products_to_discount:
        for product in products_to_discount:
            product.old_price = product.price
            product.price = product.price - (product.price * DISCOUNT)
            product.save()
