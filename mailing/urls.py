from mailing.apps import MailingConfig
from .views import (MailingCreateView, MailingDeleteView, MailingDetailView, MailingUpdateView, MailingListView,
                    MailingSendView, AttemptMailingListView, AttemptMailingDetailView, MailingStatisticsView, AttemptMailingView)
from django.urls import path, include


app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
    path('<int:pk>/send/', MailingSendView.as_view(), name='send'),
    path('<int:mailing_id>/attempts/', AttemptMailingView.as_view(), name='attempt_list'),
    path('<int:mailing_id>/attempts/<int:pk>/', AttemptMailingDetailView.as_view(), name='attempt_mailing_detail'),
    path('attempts/<int:pk>/', AttemptMailingDetailView.as_view(), name='attempt_detail'),
    path('statistics/', MailingStatisticsView.as_view(), name='user_statistics'),

]
