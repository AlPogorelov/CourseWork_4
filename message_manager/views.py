from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView,  DeleteView, UpdateView, View
from .forms import MessageForm
from .models import Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_manager/message_form.html'
    success_url = reverse_lazy('message_manager:messages_list')


class MessageListView(ListView):
    model = Message
    template_name = 'message_manager/messages_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_manager/message_detail.html'
    context_object_name = 'message'
    pk_url_kwarg = 'pk'


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_manager/message_form.html'
    success_url = reverse_lazy('message_manager:messages_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_manager/message_delete.html'


