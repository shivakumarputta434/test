from django.db import models
from django.contrib.auth.models import User








# Create your models here.
class Student(models.Model):
        name=models.CharField(max_length=50)
        password=models.CharField(max_length=50)
        marks=models.IntegerField(default=0)

        @staticmethod
        def get_students():
                return Student.objects.all()

class Post(models.Model):
        post_title=models.CharField(max_length=50)
        post_body=models.CharField(max_length=500)
        stupost=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='stupost')

class Friendlist(models.Model):
        friendname=models.CharField(max_length=50)
        friendid=models.IntegerField(default=0)
        friend=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='friend')

class Submarks(models.Model):
        subname=models.CharField(max_length=50)
        submarks=models.IntegerField(default=0)
        stumarks=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='info')


class Emp(models.Model):
        name=models.CharField(max_length=50)
        marks=models.IntegerField(default=0)

class Company(models.Model):
        name=models.CharField(max_length=50)
        number=models.IntegerField(default=0)
        randnum=models.CharField(max_length=50,blank=True)

class Staff(models.Model):
        Staff_NAME=models.CharField(max_length=50)
        Staff_AGE=models.IntegerField(default=0)
        STAFF_ADDRESS=models.CharField(max_length=50)
        Monthley_Package=models.IntegerField(default=0)

class Payment(models.Model):
        Payment_ID=models.IntegerField(default=0)
        Staff_ID=models.IntegerField(default=0)
        AMOUNT=models.IntegerField(default=0)

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='images/')



class Teacher(models.Model):
        name=models.CharField(max_length=50)
        age=models.IntegerField()
        class Meta:
                abstract=True

class Contactor(Teacher):
        salary=models.IntegerField()