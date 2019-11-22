from django.contrib import admin

from .models import Customer
from .models import Property
from .models import Job

admin.site.register(Customer)
admin.site.register(Property)
admin.site.register(Job)

