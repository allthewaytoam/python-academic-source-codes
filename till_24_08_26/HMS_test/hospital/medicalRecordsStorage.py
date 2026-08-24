"""Medical record storage using file handling."""

from pathlib import Path


RECORDS_FILE = Path(__file__).with_name("medical_records.txt")


def save_record(patient_id, diagnosis, prescription):
	"""Append one medical record to the records file."""
	with RECORDS_FILE.open("a", encoding="utf-8") as file:
		file.write(f"{patient_id}|{diagnosis}|{prescription}\n")
	print("Medical record saved successfully.")


def read_records():
	"""Read and display all saved medical records."""
	if not RECORDS_FILE.exists():
		print("No medical records found.")
		return

	with RECORDS_FILE.open("r", encoding="utf-8") as file:
		records = file.readlines()

	if not records:
		print("No medical records found.")
		return

	print("\nMedical records")
	for record in records:
		patient_id, diagnosis, prescription = record.rstrip("\n").split("|", 2)
		print(
			f"Patient ID: {patient_id}, diagnosis: {diagnosis}, "
			f"prescription: {prescription}"
		)
