from django.db import models
from recipient_manager.models import MailingRecipient
from message_manager.models import Message

class Mailing(models.Model):

    date_first_sending = models.DateField(verbose_name='Дата первой отправки', blank=True, null=True)
    date_end_shipment = models.DateField(verbose_name='Дата окончание отправки', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Completed', 'Completed'),
        ('Create', 'Create'),
        ('Running', 'Running')
    ])
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    recipient = models.ManyToManyField(MailingRecipient)

    def __str__(self):
        return f'Рассылка {self.id}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class AttemptMailing(models.Model):

    attempt_date = models.DateField(verbose_name='Дата и время попытки отправки')
    status = models.CharField(max_length=20, choices=[
        ('Successful', 'Successful'),
        ('Unsuccessful', 'Unsuccessful')
    ])
    status_response = models.TextField(blank=True, null=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

