from django.contrib import admin

from invoice.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass
