from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    photos = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name