from django.db import models

class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name} || {self.email} || {self.password}'
