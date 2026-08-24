"""Doctor information stored using tuples."""


doctors = (
	(1, "Dr. Sharma", "Cardiology"),
	(2, "Dr. Khan", "Orthopedics"),
	(3, "Dr. Patel", "General Medicine"),
)


def display_doctors():
	"""Display all available doctors."""
	print("\nAvailable doctors")
	for doctor_id, name, department in doctors:
		print(f"{doctor_id}. {name} - {department}")


def doctor_exists(doctor_id):
	"""Return True when the doctor ID is available."""
	return any(doctor[0] == doctor_id for doctor in doctors)
