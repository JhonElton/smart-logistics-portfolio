# 🚚 Smart Logistics Intelligence System & Fleet Command Center

### **Final Data Science Internship Showcase Deliverable**
**Developer:** [Your Name]  
**Academic Affiliation:** Polytechnic University of the Philippines (PUP)  
**Timeline:** 13-Week Intensive Data Science & Analytics Internship (March 2026 - June 2026)

---

## 📌 Project Overview
This repository contains an end-to-end data product designed to optimize fleet operations and monitor driver behavior using telematics data. The system ingests operational metrics (average speed, scheduled route times, and aggressive driving events), calculates dynamic safety/efficiency indexes, and exposes these data insights through interactive consumer layouts and machine-readable backend interfaces.

### Core Architectural Components:
1. **Exploratory Data Analysis Layer (`analytics.ipynb`):** Houses the primary data cleaning protocols and the composite rule-based logic used to isolate driver risk variables.
2. **Interactive Fleet Dashboard (`app.py`):** A beautiful, minimalist web interface built with **Streamlit** to provide live data grids, custom metric cards, and dynamic visualizations for dispatch supervisors.
3. **Enterprise REST API Service (`main.py`):** Powered by **FastAPI**, this backend handles programmatic requests, returning serialized portfolio info and telemetry arrays in compliant JSON format.

---

## 🛠️ Tech Stack & Environment
* **Language:** Python 3.10+
* **Data Core:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Interfaces & Backends:** Streamlit, FastAPI, Uvicorn
* **Environment & Control:** VS Code, Git/GitHub, Windows PowerShell

---

## 📈 System Repository Structure
```text
data-science-resume/
│
├── app.py                     # Streamlit Frontend Dashboard Application
├── main.py                    # FastAPI Backend Gateway File
├── analytics.ipynb            # Jupyter Notebook with Data Insight Logic
├── resume.md                  # Markdown Professional Industry Resume
│
├── charts/
│   └── driver_performance.png # Matplotlib Dual-Axis Analytical Graph
│
└── README.md                  # Comprehensive System Documentation (This File)
```
---

## 🚀 Deployment & Installation Guide
To review or execute this production system locally, ensure you have Python configured, then follow these parameters:
1. Environment Setup: pip install pandas numpy streamlit fastapi uvicorn matplotlib seaborn
2. Initializing the Fleet Command Dashboard (Streamlit): python -m streamlit run app.py
Access local web portal via: **http://localhost:8501**
3. Activating the Portfolio API Gateway (FastAPI): python -m uvicorn main:app --reload
Access interactive Swagger API documentation via: **http://127.0.0.1:8000/docs**

---

## 📊 Business Rules & Optimization Insights
* **Operational Efficiency Score:** Calculated dynamically as a derivative ratio of Scheduled Time divided by Actual Delivery Time (capped at 100%).

* **Safety Risk Profiling:** Flagged as High Risk if an operator exceeds the blended urban/expressway speed limit ceiling of 75 km/h OR records >= 3 hard-braking incidents.