from django.db import models
from django.contrib.auth.models import User # For associating posts with users
from django.utils import timezone # For post date

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # Sets current time when created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If user is deleted, their posts are too

    def __str__(self):
        return self.title