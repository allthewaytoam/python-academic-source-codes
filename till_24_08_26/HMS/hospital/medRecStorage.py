import json
from pathlib import Path
from datetime import datetime
from patientReg import patients

FILE = Path("medical_records.json")


def load_records():
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        print("Warning: Medical record file could not be read.")
        return []


def save_records(records):
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    except OSError:
        print("Unable to save medical records.")
        return False

    return True


def add_record(patient_id, diagnosis, prescription, notes=""):

    if not any(patient["id"] == patient_id for patient in patients):
        print(f"Patient ID '{patient_id}' does not exist.")
        return False

    if not diagnosis.strip():
        print("Diagnosis cannot be empty.")
        return False

    records = load_records()

    record = {
        "patient_id": patient_id,
        "diagnosis": diagnosis.strip(),
        "prescription": prescription.strip(),
        "notes": notes.strip(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    records.append(record)

    if save_records(records):
        print("Medical record added successfully.")
        return True

    return False


def view_records(patient_id):

    records = load_records()

    patient_records = [
        record for record in records
        if record["patient_id"] == patient_id
    ]

    if not patient_records:
        print(f"No medical records found for '{patient_id}'.")
        return False

    print(f"\nMedical Records — {patient_id}")
    print("=" * 50)

    for record in patient_records:
        print(f"Date: {record['date']}")
        print(f"Diagnosis: {record['diagnosis']}")
        print(f"Prescription: {record['prescription']}")
        print(f"Notes: {record['notes']}")
        print("-" * 50)

    return True