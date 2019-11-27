from django.contrib import admin

from .models import Customer, Property, Job


class CustomerAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "address",
        "phone1",
        "phone2",
        "email",
        "notes"
    )


class PropertyAdmin(admin.ModelAdmin):
    search_fields = (
        "address",
        "rental",
        "notes"
        )


class JobAdmin(admin.ModelAdmin):
    search_fields = (
        "description",
        "order_date",
        "start_date",
        "notes"
        )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Job, JobAdmin)
