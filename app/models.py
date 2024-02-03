from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # New avatar field


    def __str__(self):
        return self.name