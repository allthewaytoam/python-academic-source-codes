"""Patient report generation using Python's csv library."""

import csv
from pathlib import Path


REPORT_FILE = Path(__file__).with_name("patient_report.csv")


def generate_patient_report(patients):
	"""Write all registered patients to a CSV report."""
	with REPORT_FILE.open("w", newline="", encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Patient ID", "Name", "Age", "Phone", "Problem"])

		for patient_id, patient in patients.items():
			writer.writerow(
				[
					patient_id,
					patient["name"],
					patient["age"],
					patient["phone"],
					patient["problem"],
				]
			)

	print(f"Patient report generated: {REPORT_FILE.name}")
