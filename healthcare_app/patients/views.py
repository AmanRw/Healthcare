from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Reading
from .forms import PatientForm, ReadingForm
from ai_models.glucose_model import SimpleAnomalyDetector
from django.urls import reverse

detector = SimpleAnomalyDetector()

def index(request):
    patients = Patient.objects.all()
    return render(request, "patients/index.html", {"patients": patients})

def create_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            p = form.save()
            return redirect("patients:dashboard", patient_id=p.id)
    else:
        form = PatientForm()
    return render(request, "patients/create_patient.html", {"form": form})

def add_reading(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = ReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = patient
            reading.save()

            # Fetch historical readings of same type for this patient
            hist_values = list(
                Reading.objects.filter(patient=patient, reading_type=reading.reading_type)
                .exclude(id=reading.id)
                .order_by("-timestamp")
                .values_list("value", flat=True)
            )

            # Train model if enough data
            model = detector.train(hist_values + [reading.value])  # include new reading optionally
            is_anom = detector.is_anomaly(model, reading.value)

            status = "ALERT: Abnormal reading detected!" if is_anom else "Normal"
            return redirect(reverse("patients:dashboard", kwargs={"patient_id": patient.id}) + f"?status={status}")
    else:
        form = ReadingForm()
    return render(request, "patients/input_form.html", {"form": form, "patient": patient})

def dashboard(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    readings = patient.readings.all()[:50]  # most recent 50
    status = request.GET.get("status", "")
    # compute some simple stats
    stats = {}
    for rtype, _ in Reading.READING_CHOICES:
        vals = list(patient.readings.filter(reading_type=rtype).values_list("value", flat=True))
        if vals:
            import statistics
            stats[rtype] = {
                "count": len(vals),
                "last": vals[0],
                "mean": round(statistics.mean(vals), 2),
                "stdev": round(statistics.pstdev(vals), 2) if len(vals) > 1 else 0
            }
        else:
            stats[rtype] = {"count": 0}
    return render(request, "patients/dashboard.html", {"patient": patient, "readings": readings, "status": status, "stats": stats})
