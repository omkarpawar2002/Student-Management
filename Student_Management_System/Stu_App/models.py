from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    subject = models.CharField(max_length=100)
    marks = models.FloatField()
    city = models.CharField(max_length=100,null=False)
    address = models.TextField(max_length=255,null=False)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()