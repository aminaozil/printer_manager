from django.db import models
from clients.models import Clients
from services.models import Service

class Order(models.Model):

    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Livré'),
    )

    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.service}"

