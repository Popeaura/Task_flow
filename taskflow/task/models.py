from django.db import models

# Create your models here.
class Task(models.model):
        STATUS_CHOICES = [
            ('pending','Pending'),
            ('in_progress','In progress'),
            ('completed','Completed'),
        ]
