from django.db import models

class SurveyResponse(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DEVICE_CHOICES = [
        ('P', 'Phone'),
        ('C', 'Computer'),
        ('T', 'Tablet'),
    ]

    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    favorite_genre = models.CharField(max_length=100)
    listening_hours_per_week = models.IntegerField()
    favorite_artist = models.CharField(max_length=100)
    concert_attendance = models.BooleanField()
    device_preference = models.CharField(max_length=1, choices=DEVICE_CHOICES)

    def __str__(self):
        return f"{self.age}, {self.gender}, {self.favorite_genre}"
