from django.urls import path

from .views import ListCustomer, DetailCustomer
from .views import ListProperty, DetailProperty
from .views import ListJob, DetailJob

urlpatterns = [
    path('<int:pk>/customer', DetailCustomer.as_view()),
    path('customer/', ListCustomer.as_view()),
    path('<int:pk>/property/', DetailProperty.as_view()),
    path('property/', ListProperty.as_view()),
    path('<int:pk>/job/', DetailJob.as_view()),
    path('job/', ListJob.as_view()),
]
