from django.contrib import admin

from .models import Customer, Property, Job

admin.site.register(Customer)
admin.site.register(Property)
admin.site.register(Job)