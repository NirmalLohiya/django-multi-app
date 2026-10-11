from django.db import models
from datetime import datetime


# Create your models here.
#  i have discud about the relation model like 1-1,1-m, m-1, m-m
#  in lotes of example to identify and the create but my most usfull
# first like student hand his cources
# second one is the blog and auther like post // auther and his post this time i have use 
# i have use one to many like create to mode blog and post 

# use the blog and post based
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)  # Corrected typo
    image = models.ImageField(upload_to='Blog/', default='')  # Correct default image if needed
    date = models.DateTimeField(default=datetime.now)  # Fixed the default value for DateTimeField

    def __str__(self):
        return self.title

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)  # Added on_delete argument
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=4000)  # Changed to TextField for better handling of content
    image = models.ImageField(upload_to='post/', default='')  # Correct default image if needed
    date = models.DateField()  # If you need both date and time, use DateTimeField here

    def __str__(self):
        return self.title

    


# use the student and cources based
# class Student(models.Model):
#     image = models.ImageField(upload_to='stu_image/', default="")
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     dob = models.DateField()
#     mobileno = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     # Remove the incorrect ForeignKey to Blog
#     students = models.ManyToManyField(Student)  # Many-to-many relationship with students
#     title = models.CharField(max_length=100)
#     price = models.IntegerField()
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title




# create the model MtoONe   
# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.IntegerField()
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     dob = models.DateField()
#     mobileno = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
    
#     # Many-to-one: each student belongs to one course
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

#     def __str__(self):
#         return self.name

# note
# To get all students enrolled in a specific course, you can use:
# course = Course.objects.get(id=1)  # Assume a course with ID 1
# students_in_course = course.students.all()  # Get all students in this course

# To get the course for a particular student, you can use:
# student = Student.objects.get(id=1)  # Assume a student with ID 1
# course_of_student = student.course  # Get the course this student is enrolled in




# crete mode the one to M 
# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.IntegerField()
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     dob = models.DateField()
#     mobileno = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)

#     # ForeignKey to Course: many students can belong to one course
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

#     def __str__(self):
#         return self.name

