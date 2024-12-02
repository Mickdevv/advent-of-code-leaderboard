from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"
    
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
    
    def __str__(self):
        return f"{self.user.username} | Approved: {self.approved} | Day {self.day} | Part {self.part}"