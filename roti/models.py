from django.contrib.auth.models import User
from django.db import models

class RotiModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 64)
    expired_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='BETIS_OPREC')

    def __str__(self):
        return f"{self.name} (Owner: {self.owner}) (id: {self.pk})"