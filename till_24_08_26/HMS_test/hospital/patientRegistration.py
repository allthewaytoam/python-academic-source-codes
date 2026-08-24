"""Patient registration using a dictionary."""


patients = {}


def register_patient(patient_id, name, age, phone, problem):
	"""Add or update a patient in the patient dictionary."""
	patients[patient_id] = {
		"name": name,
		"age": age,
		"phone": phone,
		"problem": problem,
	}


def find_patient(patient_id):
	"""Return a patient dictionary, or None if it is not registered."""
	return patients.get(patient_id)


def display_patients():
	"""Display all registered patients."""
	if not patients:
		print("No patients registered.")
		return

	for patient_id, patient in patients.items():
		print(
			f"{patient_id}: {patient['name']}, age {patient['age']}, "
			f"phone {patient['phone']}, problem: {patient['problem']}"
		)

