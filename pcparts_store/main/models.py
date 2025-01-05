from django.db import models
from django.conf import settings

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

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
