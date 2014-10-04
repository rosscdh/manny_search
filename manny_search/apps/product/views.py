# -*- coding: utf-8 -*-
from django.views.generic import (ListView,)

from haystack.inputs import AutoQuery

#from django.views.generic.edit import FormMixin

#from django.utils.safestring import mark_safe

#from rest_framework.renderers import JSONRenderer

from haystack.query import SQ, SearchQuerySet
from haystack.inputs import Clean

from .models import Product
from .api.serializers import ProductSerializer

import urlparse


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'

    def get_queryset(self, **kwargs):
        sq = SQ()
        if not self.request.GET.items():
            query_set = SearchQuerySet().all()

        else:

            term = Clean(self.request.GET.get('q'))
            if term:
                sq.add(SQ(content=term), SQ.OR)
                sq.add(SQ(brand_name=term), SQ.OR)

            query_set = SearchQuerySet().filter(sq)

        return ProductSerializer([o.object for o in query_set], many=True).data
