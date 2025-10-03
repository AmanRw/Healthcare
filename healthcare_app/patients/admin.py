from django.contrib import admin
from .models import Patient, Reading

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "email")

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("patient", "reading_type", "value", "timestamp")
    list_filter = ("reading_type",)
    search_fields = ("patient__name",)
