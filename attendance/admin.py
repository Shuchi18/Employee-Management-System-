from django.contrib import admin
from .models import Attendance, Performance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('employee__name',)
    
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('employee__name',)