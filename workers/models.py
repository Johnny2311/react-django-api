from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    dni = models.CharField(max_length=20, unique=True)
    deparment = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


