from django.shortcuts import render
from django.views import generic as views

from pcparts_store.main.models import Item, OrderItem


# Create your views here.
class ItemListView(views.ListView):
    model = Item
    context_object_name = 'items'
    paginate_by = 8
    template_name = 'main/home-page.html'


class CheckoutView(views.TemplateView):
    template_name = 'main/checkout-page.html'


class ItemDetailsView(views.DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'main/product-page.html'
