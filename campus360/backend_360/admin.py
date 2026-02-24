from django.contrib import admin
from .models import CampusBlock, Classroom, Course, Faculty, Student


@admin.register(CampusBlock)
class CampusBlockAdmin(admin.ModelAdmin):
    list_display = ("name", "total_classrooms", "max_capacity")
    search_fields = ("name",)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name", "block", "seating_capacity")
    list_filter = ("block",)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "max_teaching_load")
    search_fields = ("name", "department")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "course_code", "faculty", "classroom")
    list_filter = ("faculty",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "registration_number", "course", "classroom")
    search_fields = ("name", "registration_number")