from django.db import models
from products.constants import StatusChoices


class Product(models.Model):
    user = models.ForeignKey('authentication.User', models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=StatusChoices.choices(), blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                help_text="Current price of products")
    old_price = models.DecimalField(max_digits=15, decimal_places=2,
                                    help_text="Old price of products", null=True, blank=True)
    is_billed = models.BooleanField(
        default=False,
        help_text=(
            'Product is billed'
        ),
        verbose_name='is billed'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.id}, {self.name}"
