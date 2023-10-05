
from django.urls import path,include
from .views import StudentListView,CourseListView,EnrolmentListView,PerfessorListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student',StudentListView)
router.register(r'course',CourseListView)
router.register(r'enrolement',EnrolmentListView)
router.register(r'teacher',PerfessorListView)

urlpatterns = [
    path('',include(router.urls)),
    
]