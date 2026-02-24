
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from .models import CampusBlock, Classroom, Course, Faculty, Student


# -------------------------------------------------
# LOGIN VIEW
# -------------------------------------------------
def login_view(request):
    return render(request, "login.html")