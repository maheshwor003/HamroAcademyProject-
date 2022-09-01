from django.db import models

# Create your models here.


class Instructor(models.Model):
    name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=5, null=True)
    course_name = models.CharField(max_length=40, null=True)
    max_numb_students = models.CharField(max_length=65, null=True)
    instructors = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, null=True, blank=True)
