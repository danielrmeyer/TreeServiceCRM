from django.db import models
from django.utils import timezone
import datetime


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    phone1 = models.CharField(max_length=11, null=True, blank=True)
    phone2 = models.CharField(max_length=11, null=True, blank=True)
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
    description = models.TextField()
    order_date = models.DateField('Job order date')
    start_date = models.DateField("Job start date", null=True, blank=True)
    completion_date_time = models.DateTimeField("Job completions date", null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        customer_name = str(self.customer)
        property_location = str(self.property)
        description = self.description
        return f"{description} for {customer_name} at {property_location}"


class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.FloatField(null=True, blank=True)
