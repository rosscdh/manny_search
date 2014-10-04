# -*- coding: utf-8 -*-
from django.db import models

from jsonfield import JSONField


class Product(models.Model):
    brand = models.ForeignKey('product.Brand')
    name = models.CharField(max_length=255)
    data = JSONField(default={})

    def __unicode__(self):
        return u'%s' % self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField(default={})

    def __unicode__(self):
        return u'%s' % self.name