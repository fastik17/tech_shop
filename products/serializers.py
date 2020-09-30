from django.db import transaction
from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'status', 'price', 'created_at')


class CashierProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'status', 'price',)
        read_only_fields = ('id',)

    @transaction.atomic
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        product = super().create(validated_data)
        return product


class SellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'status',)
        read_only_fields = ('id',)


class CashierBillProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'status', 'is_billed',)
        read_only_fields = ('id',)


class AccountantProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'description', 'status', 'price', 'old_price', 'is_billed',
                  'created_at', 'last_updated_at')
        read_only_fields = ('id', 'user')
