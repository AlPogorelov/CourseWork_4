from django.utils import timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView, View
from .forms import MailingForm
from .models import Mailing, AttemptMailing
from django.http import HttpResponse
from django.core.management import call_command


class MailingCreateView(CreateView):

    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.status = 'Create'
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'
    context_object_name = 'mailings'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'mailing'
    pk_url_kwarg = 'pk'


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing/mailing_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingSendView(DetailView):
    model = Mailing
    pk_url_kwarg = 'pk'
    template_name = 'mailing/mailing_send.html'

    def get(self, request, *args, **kwargs):
        mailing = self.get_object()
        return render(request, self.template_name, {'mailing': mailing})

    def save_attempt(self, mailing, status, status_response=None, recipient=None):
        attempt = AttemptMailing(mailing=mailing, attempt_date=timezone.now(), status=status)

        if recipient:
            attempt.status_response.append(f'{recipient} {status_response}')

        elif status_response:
            attempt.status_response = status_response

        attempt.save()

    def post(self, request, *args, **kwargs):
        mailing = self.get_object()

        try:
            call_command('send_mailing', mailing.pk)
            return HttpResponse('Рассылка успешно отправлена', status=200)

        except Exception as e:

            self.save_attempt(mailing, 'Unsuccessful', e)
            return HttpResponse('Ошибка при отправке рассылки', status=500)


class AttemptMailingListView(ListView):
    model = AttemptMailing
    template_name = 'attempt/attempt_list.html'
    context_object_name = 'attempts'


class AttemptMailingDetailView(DetailView):
    model = AttemptMailing
    template_name = 'attempt/attempt_detail.html'
    context_object_name = 'attempt'
    pk_url_kwarg = 'pk'

