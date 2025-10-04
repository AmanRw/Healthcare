# 🧠 AI Healthcare Monitoring & Diagnostic System

A Django-based healthcare web application that allows doctors or administrators to **monitor patient vitals**, **record medical readings**, and **upload diagnostic images** for AI-assisted evaluation.

---

## 🚀 Features

- 👨‍⚕️ **Patient Management** – Add, view, and manage patient information  
- 📊 **Vital Readings Dashboard** – Record patient readings (e.g., heart rate, BP, temperature)  
- 🧩 **AI Diagnostic Upload** – Upload X-rays or medical images for automated analysis  
- 🧠 **AI Simulation** – Currently uses a random AI result (Normal / Abnormal) for testing  
- 🧾 **Statistics Overview** – Shows patient reading count, mean, last reading, etc.  

---

## 🏗️ Project Structure

healthcare_app/
├── manage.py
├── healthcare_app/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── patients/
│ ├── migrations/
│ ├── templates/
│ │ └── patients/
│ │ ├── index.html
│ │ ├── dashboard.html
│ │ ├── input_reading.html
│ │ └── upload_diagnostic.html
│ ├── static/ (optional)
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
└── requirements.txt
