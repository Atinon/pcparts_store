from django.core import validators as django_validators
from django.db import models
from django.contrib.auth import models as auth_models

from pcparts_store.accounts.managers import StoreUserManager


# Create your models here.

class StoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    EMAIL_MAX_LENGTH = 254
    EMAIL_MIN_LENGTH = 3

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        validators=(
            django_validators.MinLengthValidator(EMAIL_MIN_LENGTH),
        ),
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = StoreUserManager()

    def __str__(self):
        return self.email
