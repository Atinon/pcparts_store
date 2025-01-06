from django.urls import path

from pcparts_store.main.views import ItemListView, CheckoutView, ItemDetailsView, add_to_cart, remove_from_cart, \
    CartView

urlpatterns = [
    path('', ItemListView.as_view(), name='home-page'),
    path('checkout', CheckoutView.as_view(), name='checkout-page'),
    path('product/<int:pk>', ItemDetailsView.as_view(), name='product-page'),
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart-page'),
    path('remove-from-cart/<int:pk>', remove_from_cart, name='remove-from-cart-page'),
    path('cart/', CartView.as_view(), name='cart-page'),
]
