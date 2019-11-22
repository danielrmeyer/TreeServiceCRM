from rest_framework import generics

from .models import Customer, Property, Job
from .serializers import CustomerSerializer, PropertySerializer, JobSerializer


class ListCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DetailCustomer(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ListProperty(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class DetailProperty(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ListJob(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class DetailJob(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
