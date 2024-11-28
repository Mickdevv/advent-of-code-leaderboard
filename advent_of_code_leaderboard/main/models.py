from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Submission(models.Model):
    DAY_CHOICES = [(i, f"Day {i}") for i in range(1, 26)]  # Dropdown for days 1 to 25
    PART_CHOICES = [(1, "Part 1"), (2, "Part 2")]  # Dropdown for parts

    createdAt = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')
    day = models.IntegerField(choices=DAY_CHOICES)
    part = models.IntegerField(choices=PART_CHOICES)
    code = models.FileField(upload_to='uploads/text_files/')