from datetime import datetime

from django import template

register = template.Library()


# @register.filter
# def row_styler(invoice_date):
#     today = datetime.datetime.today()
#     if invoice_date - today > 7:
#         return 'due'
#     if invoce_date - date in range(3,7):
#         return 'almost-due'
#     else:
#         return 'new'
#     return mark_safe(style)


@register.filter
def row_styler(invoice_date):
    today = datetime.datetime.today()
    print(today)
    # if invoice_date - today > 7:
    #     return 'due'
    # if invoce_date - date in range(3, 7):
    #     return 'almost-due'
    # else:
    #     return 'new'
    # return mark_safe(style)