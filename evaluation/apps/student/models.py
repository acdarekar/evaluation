from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.


class Student(models.Model):
    """Base Class for Model"""
    name = models.CharField(max_length=99)
    standard = models.CharField(max_length=10)
    marks = models.IntegerField()

    def get_absolute_url(self):
        return reverse('student:create_student')

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
