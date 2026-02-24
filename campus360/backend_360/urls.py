from django.urls import path
from . import views

urlpatterns = [

    # ---------------------------
    # AUTH
    # ---------------------------
    path("", views.login_view, name="login"),

    # ---------------------------
    # DASHBOARD
    # ---------------------------
    path("dashboard/", views.dashboard, name="dashboard"),

    # ---------------------------
    # CAMPUS BLOCKS
    # ---------------------------
    path("blocks/", views.blocks_view, name="blocks"),

    # ---------------------------
    # CLASSROOMS
    # ---------------------------
    path("classrooms/", views.classrooms_view, name="classrooms"),

    # ---------------------------
    # COURSES
    # ---------------------------
    path("courses/", views.courses_view, name="courses"),

    # ---------------------------
    # FACULTY
    # ---------------------------
    path("faculty/", views.faculty_view, name="faculty"),

    # ---------------------------
    # STUDENTS
    # ---------------------------
    path("students/", views.students_view, name="students"),

    # ---------------------------
    # ANALYTICS
    # ---------------------------
    path("analytics/", views.analytics_view, name="analytics"),
]