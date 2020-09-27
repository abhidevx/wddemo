# imports
import json
import redis
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer

# declaring redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

# Customer Api viewset
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer

    # Retrieving customer data from redis and setting data into redis if not present.
    def retrieve(self, request, pk=None):
        value = redis_instance.get(pk)
        if value:
            return Response(json.loads(value.decode('utf-8')))
        else:
            queryset = Customer.objects.all()
            customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(customer)
            redis_instance.set(pk, json.dumps(serializer.data))
            return Response(serializer.data)

    # getting customer data on the basis of parameters (Id,Name,slug)
    def list(self, request, *args, **kwargs):
        custmer = None
        if 'id' in request.query_params: 
            custmer = Customer.objects.filter(Q(id=request.query_params["id"]))
        if 'name' in request.query_params: 
            custmer = Customer.objects.filter(Q(name=request.query_params["name"]))
        if 'slug' in request.query_params: 
            custmer = Customer.objects.filter(Q(slug=request.query_params["slug"]))
        if not request.query_params:
               custmer = Customer.objects.all()
        serializer = CustomerSerializer(custmer, many=True)
        return Response(serializer.data)

