from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportMixin


# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city", "marks", "pass_date"]
