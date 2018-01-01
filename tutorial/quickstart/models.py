# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)

	def __str__(self):
			return self.name
			
class Product(models.Model):
	productName = models.CharField(max_length=45)
	detail = models.CharField(max_length=100)
	pricePerUnit = models.IntegerField()
	
	def __str__(self):
			return self.productName
			
class Orders(models.Model):
	productid = models.IntegerField()
	buyerId = models.IntegerField()
	sellerId = models.IntegerField()
	quantity = models.IntegerField()
	dateOrder = models.DateField()
	dateComplete = models.DateField()

	def __str__(self):
			return self.productid
	