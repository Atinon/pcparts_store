from django.urls import path

from pcparts_store.main.views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view(), name='items-list'),
]
