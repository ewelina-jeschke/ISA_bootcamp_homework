from django.db.models import Sum
from django.views.generic import ListView

from invoice.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_table.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['suma'] = Invoice.objects.aggregate(Sum('amount'))
        return context
