from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('CT', 'Contract'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_joined = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    employment_status = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_STATUS_CHOICES,
        default='FT',
    )
    
    def __str__(self):
        return f"{self.name} ({self.department})"
    