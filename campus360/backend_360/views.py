
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from .models import CampusBlock, Classroom, Course, Faculty, Student


# -------------------------------------------------
# LOGIN VIEW
# -------------------------------------------------
def login_view(request):
    return render(request, "login.html")

# --------------------------------------------------
# DASHBOARD VIEW
# --------------------------------------------------
def dashboard(request):
    total_blocks = CampusBlock.objects.count()
    total_classrooms = Classroom.objects.count()
    total_courses = Course.objects.count()
    total_faculty = Faculty.objects.count()
    total_students = Student.objects.count()

    context = {
        "total_blocks": total_blocks,
        "total_classrooms": total_classrooms,
        "total_courses": total_courses,
        "total_faculty": total_faculty,
        "total_students": total_students,
    }

    return render(request, "index.html", context)