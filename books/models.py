from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    num_pages = models.IntegerField()
    publisher = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.title}"