from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=15)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=300, default='not available')

    def __str__(self):
        return self.name 