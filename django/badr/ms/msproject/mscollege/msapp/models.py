from msilib.schema import Class
from pickle import FALSE
from re import T
from telnetlib import STATUS
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    HOD = '1' 
    STAFF = '2'  
    STUDENT = '3'  

    EMAIL_TO_USER_TYPE_MAP = {
        'hod':HOD,
        'staff':STAFF,
        'student':STUDENT
    }      
    user_type_data = ((HOD,"HOD"),(STAFF,"Staff"),(STUDENT,"Student"))
    user_type = models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager


class Courses(models.Model): 
        id = models.AutoField(primary_key=True)
        course_name = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now_add=True)
        objects = models.Manager  
           

class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


class Students(models.Model):
       id = models.AutoField(primary_key=True)
       admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
       gender = models.CharField(max_length=50)
       profile_pic = models.FileField()
       address = models.TextField()
       course_id = models.ForeignKey(Courses,on_delete=models.DO_NOTHING,default=1)
       session_year_id = models.ForeignKey(SessionYearModel,on_delete=models.CASCADE,null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now_add=True)
       objects = models.Manager 


class Staffs(models.Model):    
      id = models.AutoField(primary_key=True)
      admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
      address = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now_add=True)
      objects = models.Manager

class Subjects(models.Model):
      id =models.AutoField(primary_key=True)
      subject_name = models.CharField(max_length=255)
      course_id = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
      staff_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = models.manager



class Attendance(models.Model):     
      id = models.AutoField(primary_key=True)
      subject_id = models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
      attendance_date = models.DateField()
      session_year_id = models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = models.manager

class AttendanceReport(models.Model):
      id = models.AutoField(primary_key=True)
      student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
      attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
      status = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = models.Manager()

class StudentResult(models.Model):
     id = models.AutoField(primary_key=True)
     student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
     subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, default=1)
     subject_exam_marks = models.FloatField(default=0)
     subject_assignment_marks = models.FloatField(default=0)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = models.Manager()

class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()  


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()      



