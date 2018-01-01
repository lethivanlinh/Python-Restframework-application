from django.contrib.auth.models import User, Group
from .models import Company
from .models import Product
from .models import Orders
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
		
class CompanySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Company
		fields = ('url', 'name', 'address')
		
class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields=('url', 'productName', 'detail', 'pricePerUnit')
		
class OrdersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Orders
		fields=('url', 'productid', 'buyerId', 'sellerId','quantity','dateOrder','dateComplete')