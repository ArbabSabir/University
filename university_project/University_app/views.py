from django.shortcuts import render
from .models import StudentModel,CourseModel,ProfessorModel,EnromentModel
from .serializers import StudentSerializers,CourseSerializers,PerfessorSerializers,EnromentSerializers
from rest_framework import viewsets

# Create your views here.
class StudentListView(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

class CourseListView(viewsets.ModelViewSet):
    queryset=CourseModel.objects.all()
    serializer_class=CourseSerializers

class PerfessorListView(viewsets.ModelViewSet):
    queryset=ProfessorModel.objects.all()
    serializer_class=PerfessorSerializers

class EnrolmentListView(viewsets.ModelViewSet):
    queryset=EnromentModel.objects.all()
    serializer_class=EnromentSerializers