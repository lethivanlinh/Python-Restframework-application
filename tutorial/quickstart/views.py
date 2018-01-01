from django.contrib.auth.models import User, Group
from .models import Company
from .models import Product
from .models import Orders
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, ProductSerializer, OrdersSerializer, CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
class CompanyViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows companies to be viewed or edited.
	"""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	
class ProductViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows companies to be viewed or edited.
	"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	
class OrdersViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows companies to be viewed or edited.
	"""
	queryset = Orders.objects.all()
	serializer_class = OrdersSerializer