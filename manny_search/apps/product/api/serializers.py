# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')
    class Meta:
        model = Product