from django.urls import path

from api import views

urlpatterns = [
    path("contacts/", views.ContactAddView.as_view(), name='contacts_add'),
]