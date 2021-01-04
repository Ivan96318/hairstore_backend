from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length = 100,null = False)
    cost = models.FloatField(null = False)

class HireType(models.Model):
    name        = models.CharField(max_length = 100,null = False)
    description = models.CharField(max_length = 200,null = False)

class Employee(models.Model):
    first_name   = models.CharField(max_length = 100,null = False)
    last_name    = models.CharField(max_length = 100,null = False)
    phone_number = models.IntegerField(null = True)
    hire_type    = models.ForeignKey(HireType,null = False,on_delete = models.DO_NOTHING)
    salary       = models.FloatField(null = True)

class Job(models.Model):
    name       = models.CharField(max_length = 100, null = False)
    cost       = models.FloatField(null = False)
    percentage = models.IntegerField(null = False)

class Customer(models.Model):
    first_name   = models.CharField(max_length = 100, null = False)
    last_name    = models.CharField(max_length = 100,null = False)
    phone_number = models.IntegerField(null = True)
    promo        = models.BooleanField(null = False, default = True)
    qry_jobs     = models.IntegerField(null = True)

class Sale(models.Model):
    job_date = models.DateTimeField(auto_now_add = True,null = False)
    employee = models.ForeignKey(Employee,null = False,on_delete = models.DO_NOTHING)
    customer = models.ForeignKey(Customer,null = False,on_delete = models.DO_NOTHING)
    job      = models.ForeignKey(Job,null = False,on_delete = models.DO_NOTHING)

class Payroll(models.Model):
    type         = models.CharField(max_length = 100,null = False)
    date_payroll = models.DateTimeField(auto_now_add = True)
    total        = models.FloatField(null = False)
