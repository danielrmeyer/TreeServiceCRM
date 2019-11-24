from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import Http404
from .models import Customer, Property, Job


class IndexView(generic.TemplateView):
    template_name = 'customers/index.html'


class CustomerListView(generic.ListView):
    template_name = 'customers/customers.html'
    context_object_name = 'customers'

    def get_queryset(self, **kwargs):
        search_string = self.request.GET.get('search_string')
        axis = self.request.GET.get('axis')
        if search_string is None:
            return Customer.objects.all()

        #  name is the default search axis
        if axis == "name" or axis is None:
            customer_list = Customer.objects.filter(name__icontains=search_string)
        elif axis == "address":
            customer_list = Customer.objects.filter(address__icontains=search_string)
        elif axis == "email":
            customer_list = Customer.objects.filter(email__icontains=search_string)
        elif axis == "notes":
            customer_list = Customer.objects.filter(notes__icontains=search_string)
        else:
            raise Http404("You are searching an axis that does not exist.")

        return customer_list


class PropertyListView(generic.ListView):
    template_name = 'customers/properties.html'
    context_object_name = 'properties'

    def get_queryset(self):
        search_string = self.request.GET.get('search_string')
        axis = self.request.GET.get('axis')
        if search_string is None or search_string is "":
            return Property.objects.all()

        #  address is the default search axis
        if axis == "address" or axis is None:
            property_list = Property.objects.filter(address__icontains=search_string)
        elif axis == "notes":
            property_list = Property.objects.filter(notes__icontains=search_string)
        else:
            raise Http404("You are searching an axis that does not exist.")

        return property_list


class JobListView(generic.ListView):
    template_name = 'customers/jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        search_string = self.request.GET.get('search_string')
        axis = self.request.GET.get('axis')
        if search_string is None or search_string is "":
            return Property.objects.all()

        if axis == "description" or axis is None:
            job_list = Job.objects.filter(description__icontains=search_string)
        elif axis == "notes":
            job_list = Job.objects.filter(notes__icontains=search_string)
        else:
            raise Http404("You are searching an axis that does not exist")


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/customer.html'


class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = 'customers/property.html'


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'customers/job.html'
