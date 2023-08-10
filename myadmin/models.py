from django.db import models

# Create your models here.

class Notices(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)