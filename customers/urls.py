from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('customers', views.CustomerListView.as_view(), name='customers'),
    path('properties', views.PropertyListView.as_view(), name='properties'),
    path('jobs', views.JobListView.as_view(), name='jobs'),
    path('<int:pk>/customer', views.CustomerDetailView.as_view(), name='customer detail'),
    path('<int:pk>/property', views.PropertyDetailView.as_view(), name='property detail'),
    path('<int:pk>/job', views.JobDetailView.as_view(), name='job detail'),
]