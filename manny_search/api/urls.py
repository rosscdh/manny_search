# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

#from rest_framework import routers

from manny_search.apps.product.api.views import (ProductEndpoint,)


#router = routers.SimpleRouter(trailing_slash=True)

"""
"""

urlpatterns = patterns('',

    url(r'^products/$', ProductEndpoint.as_view(), name='product'),
)
