from datetime import datetime
from patientReg import patients
from docInfo import doctors

appointments = []


def schedule_appointment(patient_id, doctor_id, date, time):

    if not any(patient["id"] == patient_id for patient in patients):
        print(f"Patient ID '{patient_id}' does not exist.")
        return False

    if not any(doctor[0] == doctor_id for doctor in doctors):
        print(f"Doctor ID '{doctor_id}' does not exist.")
        return False

    try:
        appointment_datetime = datetime.strptime(
            f"{date} {time}", "%Y-%m-%d %H:%M"
        )
    except ValueError:
        print("Invalid date/time. Use YYYY-MM-DD and HH:MM.")
        return False

    if appointment_datetime < datetime.now():
        print("Appointment cannot be scheduled in the past.")
        return False

    for appointment in appointments:
        if (
            appointment["doctor_id"] == doctor_id
            and appointment["date"] == date
            and appointment["time"] == time
            and appointment["status"] == "Scheduled"
        ):
            print("Doctor is already booked at this time.")
            return False

    appointment_id = f"A{len(appointments) + 1:03d}"

    appointments.append({
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Scheduled"
    })

    print(f"Appointment '{appointment_id}' scheduled successfully.")
    return True


def display_appointments():

    if not appointments:
        print("No appointments available.")
        return False

    print("\nAppointments")
    print("=" * 70)

    for appointment in appointments:
        print(
            f"ID: {appointment['id']} | "
            f"Patient: {appointment['patient_id']} | "
            f"Doctor: {appointment['doctor_id']} | "
            f"{appointment['date']} {appointment['time']} | "
            f"{appointment['status']}"
        )

    return True


def cancel_appointment(appointment_id):

    for appointment in appointments:
        if appointment["id"] == appointment_id:

            if appointment["status"] == "Cancelled":
                print("Appointment is already cancelled.")
                return False

            appointment["status"] = "Cancelled"
            print(f"Appointment '{appointment_id}' cancelled successfully.")
            return True

    print(f"Appointment '{appointment_id}' does not exist.")
    return False