import os

from django.contrib import admin
from .models import Contact, Telephone

from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv('GREEN_API_INSTANCE_ID')
TOKEN = os.getenv('GREEN_API_TOKEN')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'phone', 'visit_form', 'club', 'created_at')
    list_filter = ('created_at', 'visit_form', 'club')
    search_fields = ('name', 'phone')

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    model = Telephone
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')

