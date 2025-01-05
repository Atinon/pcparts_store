from django.urls import path

from pcparts_store.main.views import ItemListView, CheckoutView, ItemDetailsView

urlpatterns = [
    path('', ItemListView.as_view(), name='home-page'),
    path('checkout', CheckoutView.as_view(), name='checkout-page'),
    path('product/<int:pk>', ItemDetailsView.as_view(), name='product-page'),
]
