from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee
from attendance.models import Attendance, Performance
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Seeds the database with fake data'

    def handle(self, *args, **options):
        fake = Faker()

        # Clear existing data (optional)
        Department.objects.all().delete()
        Employee.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()

        # 1. Create Departments
        departments = ['HR', 'Engineering',
                       'Marketing', 'Finance', 'Operations']
        for dept in departments:
            Department.objects.create(name=dept)
        self.stdout.write(self.style.SUCCESS('Created departments'))

        # 2. Create Employees (30-50 records)
        depts = list(Department.objects.all())
        for _ in range(40):  # Adjust count as needed
            Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:15],
                address=fake.address(),
                date_joined=fake.date_between(
                    start_date='-5y', end_date='today'),
                department=random.choice(depts),
                employment_status=random.choice(['FT', 'PT', 'CN'])
            )
        self.stdout.write(self.style.SUCCESS('Created employees'))

        # 3. Create Attendance Records (3 months of data)
        employees = Employee.objects.all()
        for employee in employees:
            for day in range(90):  # 90 days back
                date = datetime.now().date() - timedelta(days=day)
                status = random.choices(
                    ['P', 'A', 'L'],
                    # 80% Present, 15% Absent, 5% Late
                    weights=[0.8, 0.15, 0.05],
                    k=1
                )[0]
                Attendance.objects.create(
                    employee=employee,
                    date=date,
                    status=status
                )
        self.stdout.write(self.style.SUCCESS('Created attendance records'))

        # 4. Create Performance Reviews (1 per employee per year)
        for employee in employees:
            for year in range(1, 4):  # Last 3 years
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(
                        start_date=f'-{year}y',
                        end_date=f'-{year-1}y'
                    ),
                    comments=fake.paragraph()
                )
        self.stdout.write(self.style.SUCCESS('Created performance records'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))