# -*- coding: utf-8 -*-
#from django.conf import settings

#from rest_framework import viewsets
from rest_framework import generics

from haystack.inputs import Clean
#from haystack.inputs import AutoQuery
from haystack.query import SQ, SearchQuerySet

from ..models import (Product,)
from .serializers import (ProductSerializer,)


class ProductEndpoint(generics.ListAPIView):
    """
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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

        return [o.object for o in query_set]