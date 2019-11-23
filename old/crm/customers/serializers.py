from rest_framework import serializers
from .models import Customer, Property, Job


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'mailing_address', 'phone1', 'phone2', 'email', 'notes')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('customer', 'address', 'rental', 'notes')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('customer', 'property',
                  'description', 'order_date',
                  'start_date_time', 'completion_date_time',
                  'cost', 'notes')

