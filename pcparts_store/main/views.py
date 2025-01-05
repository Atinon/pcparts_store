from django.shortcuts import render
from django.views import generic as views

from pcparts_store.main.models import Item


# Create your views here.
class ItemListView(views.ListView):
    model = Item
    context_object_name = 'items'
    paginate_by = 10
    template_name = 'main/items_list.html'