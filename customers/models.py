from django.db import models
from django.utils import timezone
import datetime


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    phone1 = models.CharField(max_length=12, null=True, blank=True)
    phone2 = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    rental = models.BooleanField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address


class Job(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    completion_date = models.DateField("Job completion date", null=True, blank=True)
    grand_total = models.FloatField(null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        customer_name = str(self.customer)
        property_location = str(self.property)
        return f"Work for {customer_name} at {property_location}"


class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    number = models.FloatField(null=True, blank=True)
    activity = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=75, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    
