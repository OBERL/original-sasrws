from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Approved', 'Approved'),
)

CAR_STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Not Active', 'Not Active'),
)


class USR(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=True)

class Department(models.Model):
    DepartmentName = models.CharField(max_length=250)
    HeadOfDepartment = models.CharField(max_length=250)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    DepartmentId = models.CharField(max_length=250, primary_key=True)

    def __str__(self):
        return self.DepartmentName

class Employee(models.Model):
    user = models.OneToOneField(USR, on_delete=models.CASCADE, related_name='employee_profile', default=None)
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    FullName = models.CharField(max_length=250)
    EmployeeID = models.CharField(max_length=250, primary_key=True)
    DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName

class Customer(models.Model):
    user = models.OneToOneField(USR, on_delete=models.CASCADE, related_name='customer_profile', default=None)
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    FullName = models.CharField(max_length=250)
    CustomerID = models.CharField(max_length=250, primary_key=True)
    Resident = models.CharField(max_length=250)
    PhoneNumber = models.CharField(max_length=250)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    DateOfBirth = models.DateTimeField(auto_now=False)
    PassportSize = models.ImageField(upload_to='Passports/')
    CarID = models.ImageField(upload_to='Documents/')

    def __str__(self):
        return self.FirstName + " " + self.LastName

class Car(models.Model):
    CarID = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    services = models.ManyToManyField('Service', through='ServiceRecord')
    last_serviced_distance = models.FloatField(null=True, blank=True)
    PaymentAmount = models.FloatField()
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50, null=True, choices=STATUS_CHOICES, default='Pending')
    CarStatus = models.CharField(max_length=50, null=True, choices=CAR_STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.CarID

class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name

class ServiceRecord(models.Model):
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.vehicle.CarID} - {self.service.name} - {self.date}"

class Reminder(models.Model):
    driver = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    sent = models.BooleanField(default=False)
    last_serviced_distance = models.FloatField(null=True, blank=True)
    next_service_distance = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Reminder for {self.driver.FirstName} - {self.vehicle.CarID} - {self.service.name}"

class DistanceData(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    distance = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.CarID} - {self.distance} - {self.timestamp}"

    @staticmethod
    def check_service_reminders():
        cars = Car.objects.all()
        for car in cars:
            if car.last_serviced_distance is not None:
                target_distance = car.last_serviced_distance + 0.75 * (calculate_next_service_distance(car) - car.last_serviced_distance)
                current_distance = get_current_distance(car)
                percentage_traveled = (current_distance - car.last_serviced_distance) / (target_distance - car.last_serviced_distance)
                if percentage_traveled >= 0.75:
                    reminder = Reminder.objects.create(
                        driver=car.customer,
                        vehicle=car,
                        service=Service.objects.get(name="Your Service Name"),  # Replace "Your Service Name" with the actual service name
                        reminder_date=timezone.now(),
                        last_serviced_distance=car.last_serviced_distance,
                        next_service_distance=target_distance,
                    )
                    # Send reminder notification to the customer
