"""Appointment scheduling using a list."""

from .....HMS_test.hospital import doctorInfo, patientRegistration


appointments = []


def schedule_appointment(patient_id, doctor_id, date, time):
	"""Add an appointment after checking the patient and doctor IDs."""
	if patientRegistration.find_patient(patient_id) is None:
		print("Patient is not registered.")
		return False

	if not doctorInfo.doctor_exists(doctor_id):
		print("Doctor ID does not exist.")
		return False

	appointments.append(
		{
			"patient_id": patient_id,
			"doctor_id": doctor_id,
			"date": date,
			"time": time,
		}
	)
	print("Appointment scheduled successfully.")
	return True


def display_appointments():
	"""Display all scheduled appointments."""
	if not appointments:
		print("No appointments scheduled.")
		return

	for appointment in appointments:
		patient = patientRegistration.find_patient(appointment["patient_id"])
		patient_name = patient["name"] if patient else "Unknown"
		print(
			f"Patient: {patient_name} ({appointment['patient_id']}), "
			f"doctor ID: {appointment['doctor_id']}, "
			f"date: {appointment['date']}, time: {appointment['time']}"
		)
