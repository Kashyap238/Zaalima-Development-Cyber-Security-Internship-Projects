Project 3 Testing Guide

1. Start FastAPI Server

uvicorn api:app --reload

2. Open Browser

http://127.0.0.1:8000/docs

3. Test Endpoints

/dashboard
/project_status
/containment_status
/forensic_status
/incident_response_status

4. Run Simulations

python ransomware_simulation.py

5. Generate Report

python final_report.py