from django.db import models

from message_manager.models import Message


class MailingRecipient(models.Model):

    email = models.EmailField(unique=True, verbose_name='Email')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(blank=True, null=True)


