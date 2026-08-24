"""Patient billing using a class and objects."""


class Bill:
	"""Represent a patient's hospital bill."""

	def __init__(self, patient_id, consultation_fee, medicine_fee, room_fee=0):
		self.patient_id = patient_id
		self.consultation_fee = consultation_fee
		self.medicine_fee = medicine_fee
		self.room_fee = room_fee

	def total(self):
		"""Return the total amount on the bill."""
		return self.consultation_fee + self.medicine_fee + self.room_fee

	def display(self):
		"""Display the bill details."""
		print(f"Patient ID: {self.patient_id}")
		print(f"Consultation fee: {self.consultation_fee:.2f}")
		print(f"Medicine fee: {self.medicine_fee:.2f}")
		print(f"Room fee: {self.room_fee:.2f}")
		print(f"Total: {self.total():.2f}")
