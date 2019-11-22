from django.urls import path

from .views import ListCustomer, DetailCustomer

urlpatterns = [
    path('<int:pk>/', DetailCustomer.as_view()),
    path('', ListCustomer.as_view()),
]
