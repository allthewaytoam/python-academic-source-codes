from hospital import appointmentScheduling, billingSystem, docInfo, medRecStorage, patientReg, reportGen


def reg_patient():
    patient_id = input("Enter Patient ID: ").strip()
    name = input("Enter Patient Name: ").strip()
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ").strip()
    phone = input("Enter Patient Phone Number: ").strip()
    problem = input("Enter On-Spot Mentioned Problem: ").strip()

    status = patientReg.register(
        patient_id, name, age, gender, phone, problem
    )

    print(f"Patient Registration Status: {'Success' if status else 'Failed'}")


def patient_menu():
    while True:
        print(
            "\nPatient Management\n"
            "1: Register a patient\n"
            "2: Display patient details\n"
            "3: Display all patients\n"
            "4: Remove a patient\n"
            "0: Back"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        match choice:
            case 1:
                reg_patient()
            case 2:
                patientReg.display_id(input("Enter Patient ID: ").strip())
            case 3:
                patientReg.display_all()
            case 4:
                patientReg.remove_patient(input("Enter Patient ID: ").strip())
            case 0:
                break
            case _:
                print("Invalid choice. Please try again.")


def doctor_menu():
    while True:
        print(
            "\nDoctor Management\n"
            "1: Add doctor\n"
            "2: Display doctor details\n"
            "3: Display all doctors\n"
            "4: Remove doctor\n"
            "0: Back"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        match choice:
            case 1:
                did = input("Enter Doctor ID: ").strip()
                name = input("Enter Doctor Name: ").strip()
                specialization = input("Enter Specialization: ").strip()
                docInfo.add_doc(did, name, specialization)

            case 2:
                docInfo.disp_doc(input("Enter Doctor ID: ").strip())

            case 3:
                docInfo.disp_all_doc()

            case 4:
                docInfo.rem_doc(input("Enter Doctor ID: ").strip())

            case 0:
                break

            case _:
                print("Invalid choice. Please try again.")


def appointment_menu():
    while True:
        print(
            "\nAppointment Management\n"
            "1: Schedule appointment\n"
            "2: Display appointments\n"
            "3: Cancel appointment\n"
            "0: Back"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        match choice:
            case 1:
                patient_id = input("Enter Patient ID: ").strip()
                doctor_id = input("Enter Doctor ID: ").strip()
                date = input("Enter Date (YYYY-MM-DD): ").strip()
                time = input("Enter Time (HH:MM): ").strip()

                appointmentScheduling.schedule(
                    patient_id, doctor_id, date, time
                )

            case 2:
                appointmentScheduling.display_all()

            case 3:
                appointmentScheduling.cancel(
                    input("Enter Appointment ID: ").strip()
                )

            case 0:
                break

            case _:
                print("Invalid choice. Please try again.")


def medical_record_menu():
    while True:
        print(
            "\nMedical Records\n"
            "1: Add medical record\n"
            "2: View patient medical records\n"
            "0: Back"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        match choice:
            case 1:
                patient_id = input("Enter Patient ID: ").strip()
                diagnosis = input("Enter Diagnosis: ").strip()
                prescription = input("Enter Prescription: ").strip()
                notes = input("Enter Additional Notes: ").strip()

                medRecStorage.add_record(
                    patient_id, diagnosis, prescription, notes
                )

            case 2:
                medRecStorage.view_records(
                    input("Enter Patient ID: ").strip()
                )

            case 0:
                break

            case _:
                print("Invalid choice. Please try again.")


def billing_menu():
    patient_id = input("Enter Patient ID: ").strip()

    try:
        consultation = float(input("Enter Consultation Fee: "))
        medicine = float(input("Enter Medicine Charges: "))
        tests = float(input("Enter Test Charges: "))
        room = float(input("Enter Room Charges: "))
        discount = float(input("Enter Discount: "))
    except ValueError:
        print("Charges must be valid numbers.")
        return

    bill = billingSystem.Bill(
        patient_id,
        consultation,
        medicine,
        tests,
        room,
        discount
    )

    bill.display_bill()


def report_menu():
    while True:
        print(
            "\nReport Generation\n"
            "1: Generate patient report\n"
            "2: Generate appointment report\n"
            "3: Generate medical report\n"
            "0: Back"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        match choice:
            case 1:
                reportGen.patient_report()
            case 2:
                reportGen.appointment_report()
            case 3:
                reportGen.medical_report()
            case 0:
                break
            case _:
                print("Invalid choice. Please try again.")


def menu():
    while True:
        print(
            "\nMenu\n"
            "1: Patient Management\n"
            "2: Doctor Management\n"
            "3: Appointment Scheduling\n"
            "4: Medical Records\n"
            "5: Billing System\n"
            "6: Report Generation\n"
            "0: Exit"
        )

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        match choice:
            case 1:
                patient_menu()
            case 2:
                doctor_menu()
            case 3:
                appointment_menu()
            case 4:
                medical_record_menu()
            case 5:
                billing_menu()
            case 6:
                report_menu()
            case 0:
                break
            case _:
                print("Invalid choice. Please try again.")

    print(
        "\n\t===============================\n"
        "\t|| Thank you for using AMHMS ||\n"
        "\t===============================\n"
    )


def welcome():
    print(
        "\t========================================\n"
        "\t|| AMHMS · Hospital Management System ||\n"
        "\t========================================\n"
    )


def main():
    welcome()
    menu()


if __name__ == "__main__":
    main()