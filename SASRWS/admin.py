# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import USR, Customer, Department, Employee, Car, Service, ServiceRecord, Reminder, DistanceData

@admin.register(USR)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_customer', 'is_employee')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'CustomerID', 'Resident', 'PhoneNumber', 'RegisteredDate', 'DateOfBirth', 'PassportSize', 'CarID')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentName', 'HeadOfDepartment', 'RegisteredDate', 'DepartmentId')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'FullName', 'EmployeeID', 'DepartmentId', 'RegisteredDate')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('CarID', 'customer', 'employee', 'last_serviced_distance', 'PaymentAmount', 'RegisteredDate', 'Status', 'CarStatus')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost')

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service', 'date', 'notes')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('driver', 'vehicle', 'service', 'reminder_date', 'sent', 'last_serviced_distance', 'next_service_distance')

@admin.register(DistanceData)
class DistanceDataAdmin(admin.ModelAdmin):
    list_display = ('car', 'distance', 'timestamp')
