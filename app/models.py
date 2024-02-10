from django.db import models
import datetime

class Event(models.Model):
    event_title = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    avatar = models.FileField(upload_to="avatars", max_length=255, null=True, default=None)




class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)  # Adjust max_length according to your needs
    date = models.DateField(default=datetime.date.today)
    avatar = models.FileField(upload_to="avatars", max_length=255, null=True, default=None)

