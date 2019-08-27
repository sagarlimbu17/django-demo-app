from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    age = models.IntegerField()
    weight = models.IntegerField()
    joined_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name