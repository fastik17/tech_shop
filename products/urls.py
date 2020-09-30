from rest_framework.routers import DefaultRouter

from products import views

app_name = 'products'


router = DefaultRouter()

router.register('product-account', views.AccountantProductViewSet,  basename='product-account')
router.register('product-bill', views.CashierBillProductViewSet,  basename='product-bill')
router.register('product-status', views.SellerProductViewSet,  basename='product-status')
router.register('', views.CashierProductViewSet,  basename='products')


urlpatterns = [

] + router.urls
