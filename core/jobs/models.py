from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE
                             )
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    applied_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} - {self.position} ({self.status})"
