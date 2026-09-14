import csv
from datetime import datetime
from patientReg import patients
from appointment import appointments
from medicalRecords import load_records


def generate_patient_report():

    filename = f"patient_report_{datetime.now():%Y%m%d_%H%M%S}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "id",
                "name",
                "age",
                "gender",
                "phone",
                "problem"
            ]
        )

        writer.writeheader()
        writer.writerows(patients)

    print(f"Patient report generated: {filename}")


def generate_appointment_report():

    filename = f"appointment_report_{datetime.now():%Y%m%d_%H%M%S}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        if not appointments:
            print("No appointments to report.")
            return False

        writer = csv.DictWriter(
            file,
            fieldnames=appointments[0].keys()
        )

        writer.writeheader()
        writer.writerows(appointments)

    print(f"Appointment report generated: {filename}")
    return True


def generate_medical_report():

    records = load_records()

    if not records:
        print("No medical records to report.")
        return False

    filename = f"medical_report_{datetime.now():%Y%m%d_%H%M%S}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=records[0].keys()
        )

        writer.writeheader()
        writer.writerows(records)

    print(f"Medical report generated: {filename}")
    return True