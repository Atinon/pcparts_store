from django.urls import path, include

from pcparts_store.accounts.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('logout/', UserLogoutView.as_view(), name='logout-page'),
)