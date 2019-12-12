from django.contrib import admin
from django.contrib.admin import sites


from .models import Customer, Property, Job, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 3


class PropertyInline(admin.StackedInline):
    model = Property


class JobInline(admin.StackedInline):
    model = Job


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

    # inlines = [JobInline]


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
        "completion_date",
        "notes",
        "task__description",
        "task__activity",
    )

    date_hierarchy = 'completion_date'

    list_display = (
        "get_customer_name",
        "get_property_address",
        "completion_date",
        "grand_total",
        "paid",
    )

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_property_address(self, obj):
        return obj.property.address

    get_customer_name.admin_order_field = "customer"
    get_customer_name.short_description = "Customer Name"

    get_property_address.admin_order_field = "address"
    get_property_address.short_description = "Property Address"

    inlines = [TaskInline]


class TreeCareAdmin(admin.AdminSite):
    site_header = "Simple Tree Service CRM"
    site_title = "Simple Tree Service CRM"
    site_url = None


tree_care_admin = TreeCareAdmin()
admin.site = tree_care_admin
sites.site = tree_care_admin

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Job, JobAdmin)
