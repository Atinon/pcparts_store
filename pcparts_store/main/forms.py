from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(label='Street Address', max_length=100, widget=forms.TextInput(attrs={'placeholder': '1234 Main St.'}))
    apartment_address = forms.CharField(label='Apartment Address', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartment or Suite'}))
    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )
    zip = forms.CharField(label='Zip Code', max_length=10)
    same_billing_address = forms.BooleanField(label='Same Billing Address', widget=forms.CheckboxInput, required=False)
    save_info = forms.BooleanField(label='Save Info', widget=forms.CheckboxInput, required=False)
    payment_options = forms.ChoiceField(label='Payment Options', widget=forms.RadioSelect, choices=PAYMENT_CHOICES)