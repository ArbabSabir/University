from django.contrib import admin
from University_app.views import StudentModel,CourseModel,ProfessorModel,EnromentModel


# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','rollnumber','address','active')
    search_fields=('id','rollnumber')
    

@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','ccode')
    search_fields=('name','ccode')

@admin.register(ProfessorModel)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('id','name','address','active','courses')
    search_fields=('name','id')

@admin.register(EnromentModel)
class EnrolmentAdmin(admin.ModelAdmin):
    list_display=('student','course')
    

    
    
