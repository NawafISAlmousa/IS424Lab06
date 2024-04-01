from django.db import models

# Create your models here.
class Course(models.Model):
    cid = models.CharField(max_length= 5, primary_key = True)
    def __str__(self):
        return f"{self.cid}"


class Student(models.Model):
    sid = models.CharField(max_length= 8, primary_key = True)
    firstName = models.CharField(max_length= 32)
    lastName = models.CharField(max_length = 32)
    age = models.CharField(max_length= 2)
    courses = models.ManyToManyField(Course, blank = True, related_name= "students")
    def __str__(self):
        return f"{self.sid}: {self.firstName} {self.lastName}."
