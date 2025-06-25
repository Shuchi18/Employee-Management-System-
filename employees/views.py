from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from django.views import View
from attendance.models import Attendance
from collections import defaultdict
from datetime import datetime
import json
from django.views.generic import TemplateView


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_fields = ['department', 'employment_status']


class DashboardView(View):
    def get(self, request):
        # Chart 1: Employees by Department
        dept_data = {}
        for dept in Department.objects.all():
            count = Employee.objects.filter(department=dept).count()
            if count > 0:  # Only include departments with employees
                dept_data[dept.name] = count

        # Chart 2: Monthly Attendance (last 6 months)
        monthly_attendance = {}
        for month in range(6):
            try:
                current_date = datetime.now()
                if current_date.month > month:
                    target_month = current_date.month - month
                    target_year = current_date.year
                else:
                    target_month = 12 + (current_date.month - month)
                    target_year = current_date.year - 1
                    
                month_name = datetime(target_year, target_month, 1).strftime("%b %Y")
                count = Attendance.objects.filter(
                    date__month=target_month,
                    date__year=target_year,
                    status='P'
                ).count()
                monthly_attendance[month_name] = count
            except ValueError:
                continue

        context = {
            'dept_data_json': json.dumps(dept_data),
            'attendance_data_json': json.dumps(monthly_attendance)
        }
        return render(request, 'dashboard.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = "Employee Management System"
        context['features'] = [
            "Track employee records",
            "Manage attendance",
            "View performance metrics"
        ]
        return context
