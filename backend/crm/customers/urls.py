from django.urls import path

from .views import ListCustomer, DetailCustomer
from .views import ListProperty, DetailProperty
from .views import ListJob, DetailJob

urlpatterns = [
    path('<int:customer_id>/customer/', DetailCustomer.as_view()),
    path('customer/', ListCustomer.as_view()),
    path('<int:property_id>/property/', DetailProperty.as_view()),
    path('property/', ListProperty.as_view()),
    path('<int:job_id>/job/', DetailJob.as_view()),
    path('job/', ListJob.as_view()),
]
