# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import (ProductListView,)


urlpatterns = patterns('',
    url(r'^$', ProductListView.as_view(), name='list'),
)
