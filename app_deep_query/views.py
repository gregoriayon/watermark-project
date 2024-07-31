from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum

from app_deep_query.models import SalesModel

# Create your views here.

class QueryView(TemplateView):
    template_name = "app_deep_query/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Menual code process
        # total_q = 0
        # objs = SalesModel.objects.filter(product='apple')
        # for obj in objs:
        #     total_q += obj.quantity

        total_q = SalesModel.objects.filter(product='apple').aggregate(Sum('quantity'))
        # ORM query convert into SQL query
        # SELECT SUM(quantity) FROM sales_model WHERE product = 'apple';


        context['total_quantity'] = total_q['quantity__sum'] or 0
        return context