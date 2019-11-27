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

    list_display = (
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
        "notes",
    )

    list_display = (
        "address",
        "rental",
        "notes",
        "get_customer_name"
    )

    def get_customer_name(self, obj):
        return obj.customer.name

    get_customer_name.admin_order_field = "customer"
    get_customer_name.short_description = "Customer Name"


class JobAdmin(admin.ModelAdmin):
    search_fields = (
        "description",
        "order_date",
        "start_date",
        "notes",
    )

    date_hierarchy = 'start_date'

    list_display = (
        "description",
        "order_date",
        "start_date",
        "completion_date_time",
        "cost",
        "paid",
        "get_customer_name",
        "get_property_address",
    )

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_property_address(self, obj):
        return obj.property.address

    get_customer_name.admin_order_field = "customer"
    get_customer_name.short_description = "Customer Namer"

    get_property_address.admin_order_field = "address"
    get_property_address.short_description = "Property Address"


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Job, JobAdmin)
