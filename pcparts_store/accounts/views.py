from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from pcparts_store.accounts.forms import UserRegistrationForm


# Create your views here.
class UserRegisterView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, f"User registered successfully: {form.cleaned_data.get('email')}")
        return super().form_valid(form)


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, f"User logged in successfully: {form.get_user().email}")
        return super().form_valid(form)

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = 'home-page'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "User logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
