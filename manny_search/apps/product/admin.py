# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product, Brand

admin.site.register([Product, Brand])