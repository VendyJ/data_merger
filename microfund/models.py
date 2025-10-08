from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    completed_requests = models.IntegerField(default=0)

class Student(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    requests_history = models.CharField(max_length=255)

class Request(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=50)
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_amount = models.IntegerField(default=0)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_to_end = models.DateTimeField(null=True, blank=True)

    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    donor = models.ForeignKey("Donor", on_delete=models.SET_NULL, null=True, blank=True)

class Admin(models.Model):
    name = models.CharField(max_length = 100)
    status = models.CharField(max_length=50)
    # some other things, TBD

def __str__(self):
    return self.name
