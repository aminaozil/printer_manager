from django.db import models

class Clients(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name