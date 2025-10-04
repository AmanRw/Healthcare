from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_patient, name="create_patient"),
    path("<int:pk>/input/", views.input_reading, name="input_reading"),
    path("<int:patient_id>/dashboard/", views.dashboard, name="dashboard"),
    path("<int:pk>/upload_diagnostic/", views.upload_diagnostic, name="upload_diagnostic"),
    path("diagnostic/<int:pk>/", views.diagnostic_results, name="diagnostic_results"),
]
