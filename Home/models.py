# from django.db import models

# # Create your models here.
# class Request(models.Model):
#     STATUS_CHOICES = (
#         ('processing', 'Processing'),
#         ('waiting', 'Waiting'),
#         ('completed', 'Completed'),
#     )
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
#     created_at = models.DateTimeField(auto_now_add=True)  # Add this field

# class DataEntry(models.Model):
#     data = models.TextField()

#     def __str__(self):
#         return f"DataEntry {self.id}"

from django.db import models

class Request(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'Waiting'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Request {self.id} ({self.status})'

class DataEntry(models.Model):
    data = models.TextField()

    def __str__(self):
        return f'DataEntry {self.id}'
