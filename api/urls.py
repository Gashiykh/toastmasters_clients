from django.urls import path

from api import views

urlpatterns = [
    path("contacts/", views.ContactAddView.as_view(), name='contacts_add'),
    path("broadcast/", views.BroadcastView.as_view(), name='broadcast_send'),
]