from rest_framework import serializers
from attendance.models import Attendance, Performance
from employees.serializers import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']
        
        
class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'rating', 'review_date', 'comments']
