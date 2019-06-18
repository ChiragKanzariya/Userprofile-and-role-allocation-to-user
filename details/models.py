from django.db import models
from django.contrib.auth.models import User
from django import forms


class ProfileModel(models.Model):
    ROLE_CHOICES = (
        ('A', 'Admin'),
        ('N', 'Normal')
    )

    image = models.FileField(upload_to='static/upload/', null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    designation = models.CharField(max_length=25)
    other = models.TextField(max_length=250)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Profile Page'
        verbose_name_plural = 'Profile Pages'
