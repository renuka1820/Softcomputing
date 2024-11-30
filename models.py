# models.py (users app)
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('representative', 'Representative'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# models.py (service_requests app)
from django.db import models
from users.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', limit_choices_to={'role': 'customer'})
    representative = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_requests', limit_choices_to={'role': 'representative'})
    type = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    files = models.FileField(upload_to='request_files/', null=True, blank=True)
