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
    instructors = models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):

        return self.course_name

        

class Room(models.Model):
    Room_number = models.IntegerField(primary_key=True)
    Seat_capacity = models.CharField(max_length=10, null=True)

    def __str__(self):

        return str(self.Room_number)


class Meetingtime(models.Model):
    Mid = models.IntegerField(primary_key=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    day = models.DateField()

    def __str__(self):

        return str(self.time)


class Department(models.Model):
    dept_name = models.CharField(max_length=20, null=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.dept_name


class Section(models.Model):
    Section_id = models.IntegerField(primary_key=True)
    Department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    No_of_classin_week = models.CharField(max_length=20, null=True)
    Meetingtime = models.ForeignKey(
        Meetingtime, on_delete=models.CASCADE, null=True)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    instructors = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):

        return str(self.Room)
