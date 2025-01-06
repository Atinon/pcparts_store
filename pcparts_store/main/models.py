from django.db import models
from django.conf import settings
from django.urls import reverse
from django_countries.fields import CountryField

# Create your models here.

CATEGORY_CHOICES = (
    ('OTHER', 'Other'),
    ('CPU', 'CPU'),
    ('GPU', 'GPU'),
    ('RAM', 'RAM'),
    ('MB', 'Motherboard'),
)

LABEL_CHOICES = (
    ('PR', 'primary'),
    ("SC", 'secondary'),
    ('DR', 'danger'),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default=CATEGORY_CHOICES[0][0])
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, default=LABEL_CHOICES[0][0])
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={'pk': self.pk})

    def get_label_text(self):
        if self.label == 'PR':
            return 'NEW'
        elif self.label == 'DR':
            return 'SALE'
        else:
            return ''

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, null=True, blank=True)

    def get_total_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_total_price(self):
        price = 0
        for item in self.items.all():
            price += item.get_total_price()
        return price

    def __str__(self):
        return str(self.user)

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)