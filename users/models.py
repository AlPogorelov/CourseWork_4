from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    is_confirmed = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=255, null=True, blank=True)
    password_reset_token = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions_set', blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
