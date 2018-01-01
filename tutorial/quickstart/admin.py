# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Company

admin.site.register(Company)

from .models import Product

admin.site.register(Product)

from .models import Orders

admin.site.register(Orders)