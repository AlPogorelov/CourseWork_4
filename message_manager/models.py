from django.db import models


class Message(models.Model):

    subject = models.CharField(max_length=50, verbose_name='Тема сообщения')
    body_text = models.TextField(blank=True, null=True)

