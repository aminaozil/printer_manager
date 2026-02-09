from django.contrib import admin
from .models import Clients

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone')

