from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# -------------------------------------------------
# CAMPUS BLOCK
# -------------------------------------------------
class CampusBlock(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_classrooms = models.PositiveIntegerField(default=0)
    max_capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    def current_capacity(self):
        return sum(room.seating_capacity for room in self.classrooms.all())

    def utilization_percentage(self):
        if self.max_capacity == 0:
            return 0
        return round((self.current_capacity() / self.max_capacity) * 100, 2)

    def __str__(self):
        return self.name


# -------------------------------------------------
# CLASSROOM
# -------------------------------------------------
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    block = models.ForeignKey(
        CampusBlock,
        on_delete=models.CASCADE,
        related_name='classrooms'
    )
    seating_capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    def current_students_count(self):
        return self.students.count()

    def utilization_percentage(self):
        if self.seating_capacity == 0:
            return 0
        return round(
            (self.current_students_count() / self.seating_capacity) * 100,
            2
        )

    def __str__(self):
        return f"{self.name} - {self.block.name}"


# -------------------------------------------------
# FACULTY
# -------------------------------------------------
class Faculty(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    max_teaching_load = models.PositiveIntegerField(
        help_text="Maximum teaching hours allowed"
    )

    def current_teaching_load(self):
        return sum(course.credit_hours for course in self.courses.all())

    def workload_percentage(self):
        if self.max_teaching_load == 0:
            return 0
        return round(
            (self.current_teaching_load() / self.max_teaching_load) * 100,
            2
        )

    def __str__(self):
        return self.name


# -------------------------------------------------
# COURSE
# -------------------------------------------------
class Course(models.Model):
    name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=50, unique=True)
    credit_hours = models.PositiveIntegerField()
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )

    def enrolled_students_count(self):
        return self.students.count()

    def __str__(self):
        return f"{self.name} ({self.course_code})"


# -------------------------------------------------
# STUDENT
# -------------------------------------------------
class Student(models.Model):
    name = models.CharField(max_length=150)
    registration_number = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    def __str__(self):
        return f"{self.name} - {self.registration_number}"