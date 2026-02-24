from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("blocks/", views.blocks_view, name="blocks"),
    path("classrooms/", views.classrooms_view, name="classrooms"),
    path("courses/", views.courses_view, name="courses"),
    path("faculty/", views.faculty_view, name="faculty"),
    path("students/", views.students_view, name="students"),
    path("analytics/", views.analytics_view, name="analytics"),
    path("logout/", views.logout_view, name="logout"),
]