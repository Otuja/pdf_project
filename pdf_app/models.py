from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Pdf(models.Model):
    coursename = models.CharField(max_length=30)
    coursecode = models.CharField(max_length=8, null=True, blank=True)
    upload = models.FileField(upload_to="uploads/%Y/%m/%d/")
    description = models.TextField(null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.coursecode} ({self.coursename})"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email