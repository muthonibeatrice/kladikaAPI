"""kladika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django. conf import settings
from merchant.views import MerchantList, UpdateMerchant
from mystyle.views import MyStyleList, UpdateMyStyle
from photos.views import PhotosList, UpdatePhotos
from users.views import UserList, UpdateUser
from order.views import OrderList, UpdateOrder
from payment.views import PaymentList, UpdatePayment
from products.views import ProductsList, UpdateProducts
from product_variants.views import ProductVariantsList, UpdateProductVariants
from ordered_products.views import OrderedProductsList, UpdateOrderedProducts
from product_stock.views import ProductStockList, UpdateProductStock
from product_subtype.views import ProductSubTypeList, UpdateProductSubType
from product_type.views import ProductTypeList, UpdateProductType
from store.views import StoreList, UpdateStore
from feed.views import FeedList, UpdateFeed




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/merchant', MerchantList.as_view(), name="All_the_merchants"),
    url(r'^api/merchant/(?P<pk>[0-9]+)', UpdateMerchant.as_view(), name="Update_merchant"),
    url(r'^api/stores', StoreList.as_view(), name="All_the_stores"),
    url(r'^api/stores/(?P<pk>[0-9]+)', UpdateStore.as_view(), name="Update_store"),
    url(r'^api/product-type', ProductTypeList.as_view(), name="All_product_types"),
    url(r'^api/product-type/(?P<pk>[0-9]+)', UpdateProductType.as_view(), name="Update_product_types"),
    url(r'^api/product-subtype', ProductSubTypeList.as_view(), name="All_product_subtypes"),
    url(r'^api/product-subtype/(?P<pk>[0-9]+)', UpdateProductSubType.as_view(), name="Update_product_subtypes"),
    url(r'^api/product-stock', ProductStockList.as_view(), name="All_product_stocks"),
    url(r'^api/product-stock/(?P<pk>[0-9]+)', UpdateProductStock.as_view(), name="Update_product_stock"),
    url(r'^api/mystyle', MyStyleList.as_view(), name="My_Style"),
    url(r'^api/mystyle/(?P<pk>[0-9]+)', UpdateMerchant.as_view(), name="Edit_Style"),
    url(r'^api/photos', PhotosList.as_view(), name="Store_photos"),
    url(r'^api/photos/(?P<pk>[0-9]+)', UpdatePhotos.as_view(), name="Edit_photos"),
    url(r'^api/feed', FeedList.as_view(), name="Show_feed"),
    url(r'^api/feed/(?P<pk>[0-9]+)', UpdateFeed.as_view(), name="Edit_Feed"),
    url(r'^api/users', UserList.as_view(), name="Users"),
    #url(r'^api/registration', CreateUserView.as_view(), name="Register"),
    #url(r'^api/users/(?P<pk>[0-9]+)', UpdateUser.as_view(), name="Edit_User"),
    url(r'^api/orders', OrderList.as_view(), name="Orders"),
    url(r'^api/orders/(?P<pk>[0-9]+)', UpdateOrder.as_view(), name="Edit_orders"),
    url(r'^api/payment', PaymentList.as_view(), name="Payment"),
    url(r'^api/payment/(?P<pk>[0-9]+)', PaymentList.as_view(), name="Edit_payment"),
    url(r'^api/orderered-products', OrderedProductsList.as_view(), name="orderered_products"),
    url(r'^api/orderered-products/(?P<pk>[0-9]+)', UpdateOrderedProducts.as_view(), name="orderered_products"),
    url(r'^api/product', ProductsList.as_view(), name="products"),
    url(r'^api/product/(?P<pk>[0-9]+)', UpdateProducts.as_view(), name="Edit_product"),
    url(r'^api/product-variants', ProductVariantsList.as_view(), name="product_variation"),
    url(r'^api/product-variants/(?P<pk>[0-9]+)', UpdateProductVariants.as_view(), name="Edit_product_variation")


]
