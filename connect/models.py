from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):

    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier')

    username = models.CharField(
        max_length=150, unique=True)

    email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True, default=None)

    phone_number = models.CharField(
        max_length=17, unique=True, blank=True, null=True)

    color = models.CharField(max_length=32, default="#95a5a6", blank=True)

    isconfirmed = models.BooleanField(_('Is Confirmed'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
