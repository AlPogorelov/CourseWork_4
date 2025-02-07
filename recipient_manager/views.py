from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from mailing.models import Mailing
from .forms import MailingRecipientForm
from .models import MailingRecipient
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView, View


class MailingRecipientListView(ListView):
    model = MailingRecipient
    template_name = 'recipient_manager/recipient_list.html'
    context_object_name = 'recipients'


class MailingRecipientDetailView(DetailView):
    model = MailingRecipient
    template_name = 'recipient_manager/recipient_detail.html'
    context_object_name = 'recipient'
    pk_url_kwarg = 'pk'


class MailingRecipientCreateView(CreateView):
    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = 'recipient_manager/recipient_form.html'
    success_url = reverse_lazy('recipient_manager:recipient_list')


class MailingRecipientDeleteView(DetailView):

    model = MailingRecipient
    template_name = 'recipient_manager/recipients_delete.html'
    context_object_name = 'recipient'
    pk_url_kwarg = 'pk'


class MailingRecipientUpdateView(UpdateView):

    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = 'recipient_manager/recipient_form.html'
    success_url = reverse_lazy('recipient_manager:recipient_list')


class HomeView(TemplateView):
    template_name = 'recipient_manager/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['total_mailings'] = Mailing.objects.count()


        context['active_mailings'] = Mailing.objects.filter(status='Running').count()


        context['unique_recipients'] = MailingRecipient.objects.count()  # или оптимизированный запрос

        return context