from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=39)
    rollnumber=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class FakeModel(models.Model):
    name=models.CharField(max_length=29)
class CourseModel(models.Model):
    name=models.CharField(max_length=50)
    ccode=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class ProfessorModel(models.Model):
    name=models.CharField(max_length=39)
    address=models.CharField( max_length=50)
    active=models.BooleanField(default=False)
    courses=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class EnromentModel(models.Model):
    student=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    
