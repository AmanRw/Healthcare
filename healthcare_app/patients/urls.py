from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_patient, name="create_patient"),
    path("<int:patient_id>/dashboard/", views.dashboard, name="dashboard"),
    path("<int:patient_id>/add-reading/", views.add_reading, name="add_reading"),
]
