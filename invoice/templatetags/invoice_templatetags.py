from datetime import datetime

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def row_styler(invoice, style=None):
    today = datetime.datetime.today()
    if invoice.is_paid:
        return 'paid'
    elif (invoice.payment_date - today).days < 1:
        return 'overdue'
    elif (invoice.payment_date - today).days > 7:
        return 'due'
    elif (invoice.payment_date - today).days in range(1, 7):
        return 'almost-due'

    return mark_safe(style)


