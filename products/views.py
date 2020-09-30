from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from authentication.permissions import IsCashierProfileOnly, IsSellerProfileOnly, IsAccountantProfileOnly
from products import serializers
from products.models import Product
from products.filters import DateProductFilter
from tech_shop.mixins import ListSerializerMixin
from tech_shop.paginators import ResultPagination


class CashierProductViewSet(ListSerializerMixin,
                            viewsets.ModelViewSet):
    """
    list:
    Get list of user's Products as cashier

    Get list of user's Products as cashier

    NOTE User must be `is_cashier=True` to perform this action

    retrieve:
    Retrieve user's Product as cashier

    Retrieve user's Product as cashier

    NOTE User must be `is_cashier=True` to perform this action

    create:
    Create Product object as cashier

    Create Product object as cashier

    NOTE User must be `is_cashier=True` to perform this action

    update:
    Update Product with ID as cashier

    Update Product with the given ID as cashier

    NOTE User must be `is_cashier=True` to perform this action

    partial_update:
    Partial update of Product with ID as cashier

    Partial update of Product with ID as cashier

    NOTE User must be `is_cashier=True` to perform this action

    destroy:
    Delete Product object as cashier

    Delete Product object as cashier

    NOTE User must be `is_cashier=True` to perform this action
    """
    permission_classes = (IsCashierProfileOnly,)
    list_serializer_class = serializers.ProductListSerializer
    serializer_class = serializers.CashierProductSerializer
    pagination_class = ResultPagination
    queryset = Product.objects.all()


class CashierBillProductViewSet(ListSerializerMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    """
    list:
    Get list of user's Products as cashier

    Get list of user's Products as cashier

    NOTE User must be `is_cashier=True` to perform this action

    retrieve:
    Retrieve user's Product as cashier

    Retrieve user's Product as cashier

    NOTE User must be `is_cashier=True` to perform this action

    update:
    Update Product with ID as cashier

    Update Product with the given ID as cashier

    NOTE User must be `is_cashier=True` to perform this action.
    To bill client change `is_billed=True`


    partial_update:
    Partial update of Product with ID as cashier

    Partial update of Product with ID as cashier

    NOTE User must be `is_cashier=True` to perform this action.
    To bill client change `is_billed=True`
    """
    permission_classes = (IsCashierProfileOnly,)
    list_serializer_class = serializers.ProductListSerializer
    serializer_class = serializers.CashierBillProductSerializer
    pagination_class = ResultPagination
    queryset = Product.objects.all()


class SellerProductViewSet(ListSerializerMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    """
    list:
    Get list of user's Products as seller

    Get list of user's Products as seller

    NOTE User must be `is_seller=True` to perform this action

    retrieve:
    Retrieve user's Product as seller

    Retrieve user's Product as seller

    NOTE User must be `is_seller=True` to perform this action

    update:
    Update Product with ID as seller

    Update Product with the given ID as seller

    NOTE User must be `is_seller=True` to perform this action

    partial_update:
    Partial update of Product with ID as seller

    Partial update of Product with ID as seller

    NOTE User must be `is_seller=True` to perform this action
    """
    permission_classes = (IsSellerProfileOnly,)
    list_serializer_class = serializers.ProductListSerializer
    serializer_class = serializers.SellerProductSerializer
    pagination_class = ResultPagination
    queryset = Product.objects.all()


class AccountantProductViewSet(ListSerializerMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    """
    list:
    Get list of Products as accountant

    Get list of Products as accountant

    NOTE User must be `is_accountant=True` to perform this action
    """
    permission_classes = (IsAccountantProfileOnly,)
    list_serializer_class = serializers.AccountantProductSerializers
    pagination_class = ResultPagination
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = DateProductFilter
