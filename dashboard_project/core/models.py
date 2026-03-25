from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    name = models.CharField(max_length=200)
    credits = models.IntegerField()
    def __str__(self):
        return self.name
class Enrollment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    grade = models.CharField(max_length=5, blank=True, null=True) 
    date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"

