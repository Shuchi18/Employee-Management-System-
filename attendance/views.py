from django.shortcuts import render
from rest_framework import viewsets
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_fields = ['employee', 'date', 'status']
    
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_fields = ['employee', 'rating', 'review_date']