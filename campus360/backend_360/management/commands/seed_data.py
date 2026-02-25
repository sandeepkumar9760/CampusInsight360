import random
from django.core.management.base import BaseCommand
from backend_360.models import CampusBlock, Classroom, Faculty, Course, Student


class Command(BaseCommand):
    help = "Seed database with realistic demo data"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS("Seeding data..."))

        # Clear existing data (optional)
        Student.objects.all().delete()
        Course.objects.all().delete()
        Faculty.objects.all().delete()
        Classroom.objects.all().delete()
        CampusBlock.objects.all().delete()

        # ----------- Create Blocks -----------
        blocks = []
        for name in ["A Block", "B Block", "C Block"]:
            block = CampusBlock.objects.create(
                name=name,
                total_classrooms=10,
                max_capacity=500
            )
            blocks.append(block)

        # ----------- Create Classrooms -----------
        classrooms = []
        for block in blocks:
            for i in range(1, 6):
                classroom = Classroom.objects.create(
                    name=f"{block.name} - Room {i}",
                    block=block,
                    seating_capacity=random.randint(40, 80)
                )
                classrooms.append(classroom)

        # ----------- Create Faculty -----------
        faculty_list = []
        departments = ["Computer Science", "Mathematics", "Physics", "Electronics"]

        for i in range(10):
            faculty = Faculty.objects.create(
                name=f"Faculty {i+1}",
                department=random.choice(departments),
                max_teaching_load=random.randint(3, 6)
            )
            faculty_list.append(faculty)

        # ----------- Create Courses -----------
        courses = []
        for i in range(15):
            course = Course.objects.create(
                name=f"Course {i+1}",
                course_code=f"CSE{i+100}",
                credit_hours=random.randint(2, 4),
                faculty=random.choice(faculty_list),
                classroom=random.choice(classrooms)
            )
            courses.append(course)

        # ----------- Create Students -----------
        for i in range(200):
            Student.objects.create(
                name=f"Student {i+1}",
                registration_number=f"REG2026{i+1000}",
                course=random.choice(courses),
                classroom=random.choice(classrooms)
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))