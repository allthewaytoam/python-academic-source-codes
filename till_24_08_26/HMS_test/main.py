from sc.academic.till_24_08_26.HMS_test.hospital import (
    patientRegistration,
)
from sc.academic.till_24_08_26.HMS_test.hospital import appointmentScheduling, billing, doctorInfo, generateReport, medicalRecordsStorage


def read_number(prompt, as_integer=False):
    """Read a numeric value and keep asking until it is valid."""
    while True:
        try:
            return int(input(prompt)) if as_integer else float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\nHospital Management System")
        print("1. Register patient")
        print("2. Display patients")
        print("3. Display doctors")
        print("4. Schedule appointment")
        print("5. Display appointments")
        print("6. Save medical record")
        print("7. Read medical records")
        print("8. Create bill")
        print("9. Generate patient report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = read_number("Patient ID: ", as_integer=True)
            name = input("Name: ")
            age = read_number("Age: ", as_integer=True)
            phone = input("Phone: ")
            problem = input("Medical problem: ")
            patientRegistration.register_patient(
                patient_id, name, age, phone, problem
            )
            print("Patient registered successfully.")
        elif choice == "2":
            patientRegistration.display_patients()
        elif choice == "3":
            doctorInfo.display_doctors()
        elif choice == "4":
            patient_id = read_number("Patient ID: ", as_integer=True)
            doctor_id = read_number("Doctor ID: ", as_integer=True)
            date = input("Date: ")
            time = input("Time: ")
            appointmentScheduling.schedule_appointment(
                patient_id, doctor_id, date, time
            )
        elif choice == "5":
            appointmentScheduling.display_appointments()
        elif choice == "6":
            patient_id = read_number("Patient ID: ", as_integer=True)
            diagnosis = input("Diagnosis: ")
            prescription = input("Prescription: ")
            medicalRecordsStorage.save_record(
                patient_id, diagnosis, prescription
            )
        elif choice == "7":
            medicalRecordsStorage.read_records()
        elif choice == "8":
            patient_id = read_number("Patient ID: ", as_integer=True)
            consultation_fee = read_number("Consultation fee: ")
            medicine_fee = read_number("Medicine fee: ")
            room_fee = read_number("Room fee: ")
            patient_bill = billing.Bill(
                patient_id, consultation_fee, medicine_fee, room_fee
            )
            patient_bill.display()
        elif choice == "9":
            generateReport.generate_patient_report(patientRegistration.patients)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()