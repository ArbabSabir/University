from rest_framework import serializers
from .models import StudentModel,CourseModel,ProfessorModel,EnromentModel

#make serializers
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields= '__all__'

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseModel
        fields= '__all__'
    

class PerfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProfessorModel
        fields= '__all__'
        

class EnromentSerializers(serializers.ModelSerializer):
    class Meta:
        model=EnromentModel
        fields= '__all__'