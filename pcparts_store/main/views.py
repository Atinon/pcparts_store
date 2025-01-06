from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic as views

from pcparts_store.main.forms import CheckoutForm
from pcparts_store.main.models import Item, OrderItem, Order, BillingAddress


# Create your views here.
class ItemListView(views.ListView):
    model = Item
    context_object_name = 'items'
    paginate_by = 8
    template_name = 'main/home-page.html'


class ItemDetailsView(views.DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'main/product-page.html'


class CartView(views.View):
    def get(self, request):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(self.request, 'main/cart-page.html', {'order': order})
        except ObjectDoesNotExist:
            messages.error(self.request, 'Order does not exist')
            return redirect('home-page')


def add_to_cart(request, pk):
    redirect_url = request.GET.get('redirect_url', 'product-page')
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Item quantity updated.')
        else:
            messages.info(request, 'Item added to cart.')
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=order_date)
        order.items.add(item)
        messages.info(request, 'Item added to cart.')
    return redirect(redirect_url, pk=pk)


def remove_from_cart(request, pk):
    redirect_url = request.GET.get('redirect_url', 'product-page')
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=pk).exists():
            order_item = OrderItem.objects.get(item=item, user=request.user, ordered=False)
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, 'Item removed from the cart.')
        else:
            messages.info(request, 'Item was not in the cart.')
    else:
        messages.info(request, 'You do not have an active order.')
    return redirect(redirect_url, pk=pk)


class CheckoutView(views.View):
    def get(self, request):
        form = CheckoutForm()
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(self.request, 'main/checkout-page.html', {
                'form': form,
                'order': order,
            })
        except ObjectDoesNotExist:
            messages.error(self.request, 'Order does not exist')
            return redirect('home-page')

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zipcode = form.cleaned_data.get('zip')
                # TODO
                # same_billing_address = form.cleaned_data.get('same_billing_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_options = form.cleaned_data.get('payment_options')
                billing_address = BillingAddress(
                    user=self.request.user,
                    street=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zipcode=zipcode,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                print(payment_options)
                return redirect('payment-page', payment_option=payment_options)
            messages.warning(self.request, 'Checkout form submission failed.')
            return redirect('checkout-page')
        except ObjectDoesNotExist:
            messages.error(self.request, 'Order does not exist')
            return redirect('cart-page')

class PaymentView(views.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'main/payment-page.html')
