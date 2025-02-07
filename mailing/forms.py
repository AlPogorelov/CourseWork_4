from .models import Mailing
from django import forms


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['message', 'recipient']
