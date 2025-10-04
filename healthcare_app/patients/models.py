from django.db import models
from django.utils import timezone

class Patient(models.Model):
    # In a real app you'd connect to an auth user, include identifiers, consent, etc.
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} (id={self.id})"

class Reading(models.Model):
    # For flexibility, reading_type could be 'glucose', 'heart_rate', etc.
    READING_CHOICES = [
        ("glucose", "Glucose (mg/dL)"),
        ("heart_rate", "Heart Rate (bpm)"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="readings")
    reading_type = models.CharField(max_length=32, choices=READING_CHOICES, default="glucose")
    value = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.patient.name} {self.reading_type} {self.value} at {self.timestamp}"

class HealthReading(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    heart_rate = models.IntegerField()
    glucose_level = models.FloatField()
    blood_pressure = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"

class DiagnosticImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="diagnostics/")
    result = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) # AI prediction

    def __str__(self):
        return f"{self.patient.name} - {self.result or 'Pending'}"
