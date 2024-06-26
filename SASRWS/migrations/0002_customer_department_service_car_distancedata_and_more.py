# Generated by Django 5.0.3 on 2024-05-08 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SASRWS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('FullName', models.CharField(max_length=250)),
                ('CustomerID', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('Resident', models.CharField(max_length=250)),
                ('PhoneNumber', models.CharField(max_length=250)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('DateOfBirth', models.DateTimeField()),
                ('PassportSize', models.ImageField(upload_to='Passports/')),
                ('CarID', models.ImageField(upload_to='Documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentName', models.CharField(max_length=250)),
                ('HeadOfDepartment', models.CharField(max_length=250)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('DepartmentId', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarID', models.CharField(max_length=250)),
                ('last_serviced_distance', models.FloatField(blank=True, null=True)),
                ('PaymentAmount', models.FloatField()),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Approved', 'Approved')], default='Pending', max_length=50, null=True)),
                ('CarStatus', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], default='Active', max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DistanceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.car')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('FullName', models.CharField(max_length=250)),
                ('EmployeeID', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('DepartmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.department')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.employee'),
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_date', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
                ('last_serviced_distance', models.FloatField(blank=True, null=True)),
                ('next_service_distance', models.FloatField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.car')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.service')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SASRWS.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='services',
            field=models.ManyToManyField(through='SASRWS.ServiceRecord', to='SASRWS.service'),
        ),
    ]
