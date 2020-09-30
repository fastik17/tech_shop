from django.contrib import admin

from products import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'price')
    readonly_fields = ('created_at', 'last_updated_at')
