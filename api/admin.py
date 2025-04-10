from django.contrib import admin

from .models import  Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

