from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from .models import CampusBlock, Classroom, Course, Faculty, Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# -------------------------------------------------
# LOGIN VIEW
# -------------------------------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")
# --------------------------------------------------
# DASHBOARD VIEW
# --------------------------------------------------
@login_required
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
# ----------------------------------------------------------
# BLOCK VIEW
# ----------------------------------------------------------
@login_required
def blocks_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        total_classrooms = request.POST.get("total_classrooms")
        max_capacity = request.POST.get("max_capacity")

        CampusBlock.objects.create(
            name=name,
            total_classrooms=total_classrooms,
            max_capacity=max_capacity
        )

        return redirect("blocks")

    blocks = CampusBlock.objects.all()

    context = {
        "blocks": blocks
    }

    return render(request, "blocks.html", context)

# ------------------------------------------------------
# CLASSROOM VIEW
# ------------------------------------------------------
@login_required
def classrooms_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        block_id = request.POST.get("block")
        seating_capacity = request.POST.get("seating_capacity")

        block = CampusBlock.objects.get(id=block_id)

        Classroom.objects.create(
            name=name,
            block=block,
            seating_capacity=seating_capacity
        )

        return redirect("classrooms")

    classrooms = Classroom.objects.select_related("block").all()
    blocks = CampusBlock.objects.all()

    context = {
        "classrooms": classrooms,
        "blocks": blocks,
    }

    return render(request, "classrooms.html", context)
# ----------------------------------------------------------------
# COURSES VIEW 
# ----------------------------------------------------------------
@login_required
def courses_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("course_code")
        credit_hours = request.POST.get("credit_hours")
        faculty_id = request.POST.get("faculty")
        classroom_id = request.POST.get("classroom")

        faculty = Faculty.objects.get(id=faculty_id)
        classroom = Classroom.objects.get(id=classroom_id)

        Course.objects.create(
            name=name,
            course_code=code,
            credit_hours=credit_hours,
            faculty=faculty,
            classroom=classroom
        )

        return redirect("courses")

    courses = Course.objects.select_related("faculty", "classroom").all()
    faculties = Faculty.objects.all()
    classrooms = Classroom.objects.all()

    context = {
        "courses": courses,
        "faculties": faculties,
        "classrooms": classrooms,
    }

    return render(request, "courses.html", context)

# ---------------------------------------------------------
# FACULTY VIEW 
# ---------------------------------------------------------
@login_required
def faculty_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        max_teaching_load = request.POST.get("max_teaching_load")

        Faculty.objects.create(
            name=name,
            department=department,
            max_teaching_load=max_teaching_load
        )

        return redirect("faculty")

    faculty_members = Faculty.objects.all()

    context = {
        "faculty_members": faculty_members
    }

    return render(request, "faculty.html", context)
# -------------------------------------------------------
# STUDENTS VIEW
# -------------------------------------------------------
@login_required
def students_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        reg_no = request.POST.get("registration_number")
        course_id = request.POST.get("course")
        classroom_id = request.POST.get("classroom")

        course = Course.objects.get(id=course_id)
        classroom = Classroom.objects.get(id=classroom_id)

        Student.objects.create(
            name=name,
            registration_number=reg_no,
            course=course,
            classroom=classroom
        )

        return redirect("students")

    students = Student.objects.select_related("course", "classroom").all()
    courses = Course.objects.all()
    classrooms = Classroom.objects.all()

    context = {
        "students": students,
        "courses": courses,
        "classrooms": classrooms,
    }

    return render(request, "students.html", context)
# --------------------------------------------------------
# ANALYTICS VIEW 
# --------------------------------------------------------
@login_required
def analytics_view(request):

    blocks = CampusBlock.objects.all()
    classrooms = Classroom.objects.all()
    faculty_members = Faculty.objects.all()

    # Student distribution per course
    course_distribution = Course.objects.annotate(
        student_count=Count("students")
    )

    context = {
        "blocks": blocks,
        "classrooms": classrooms,
        "faculty_members": faculty_members,
        "course_distribution": course_distribution,
    }

    return render(request, "analytics.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")