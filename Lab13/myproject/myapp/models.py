from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Person(models.Model):
    """
    Model representing a person with name, age, and creation date.
    """
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.age}"