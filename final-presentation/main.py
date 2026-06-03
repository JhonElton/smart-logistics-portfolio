from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

app = FastAPI(
    title="Smart Logistics Data Portfolio API",
    description="Production-ready REST API serving professional resume structures and fleet analytics insights.",
    version="1.0.0"
)

# Enable CORS so your future frontend dashboard applications can fetch data safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data synchronized directly with your Day 3 Streamlit App
FLEET_REGISTRY = [
    {"driver_id": "DRV-001", "name": "Driver A", "avg_speed_kph": 82, "efficiency_score": 100.0, "risk_profile": "High Risk"},
    {"driver_id": "DRV-002", "name": "Driver B", "avg_speed_kph": 58, "efficiency_score": 88.89, "risk_profile": "Normal"},
    {"driver_id": "DRV-003", "name": "Driver C", "avg_speed_kph": 94, "efficiency_score": 100.0, "risk_profile": "High Risk"},
    {"driver_id": "DRV-004", "name": "Driver D", "avg_speed_kph": 65, "efficiency_score": 92.11, "risk_profile": "Normal"},
    {"driver_id": "DRV-005", "name": "Driver E", "avg_speed_kph": 71, "efficiency_score": 100.0, "risk_profile": "Normal"}
]

@app.get("/")
def root():
    return {"message": "Welcome to Elton's Data Science Portfolio Gateway. Head over to /docs for interactive Swagger UI."}

@app.get("/api/v1/resume")
def get_resume_profile():
    """Returns candidate professional metadata and technical specializations."""
    return {
        "candidate": "Elton",
        "role": "Data Science & Analytics Intern",
        "specialization": "Smart Logistics & Fleet Telematics",
        "core_skills": ["Python", "Pandas", "FastAPI", "Streamlit", "Redis", "Machine Learning"],
        "education": {
            "institution": "Polytechnic University of the Philippines (PUP)",
            "degree": "Bachelor of Science in Information Technology",
            "expected_graduation": "2026"
        }
    }

@app.get("/api/v1/fleet", response_model=List[Dict])
def get_fleet_analytics():
    """Retrieves computed telematics records and calculated dynamic risk thresholds."""
    return FLEET_REGISTRY