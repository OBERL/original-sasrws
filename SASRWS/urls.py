
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('services/', views.services, name='services'),
    path('service_rec/', views.service_rec, name='service_rec'),
]