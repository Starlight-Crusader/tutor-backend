from django.db import models
from students.model import Student
from courses.model import Course


class Subscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
