from django.urls import path
from employee.api import views

urlpatterns = [
    path('api/employees/', views.employee_list),
    path('api/employees/<int:pk>/', views.employee_detail),
]