from datetime import datetime
from patientReg import patients


class Bill:

    def __init__(
        self,
        patient_id,
        consultation_fee=0,
        medicine_charge=0,
        test_charge=0,
        room_charge=0,
        discount=0
    ):
        self.patient_id = patient_id
        self.consultation_fee = consultation_fee
        self.medicine_charge = medicine_charge
        self.test_charge = test_charge
        self.room_charge = room_charge
        self.discount = discount
        self.created_at = datetime.now()

    def subtotal(self):
        return (
            self.consultation_fee
            + self.medicine_charge
            + self.test_charge
            + self.room_charge
        )

    def total(self):
        return max(0, self.subtotal() - self.discount)

    def generate_bill(self):

        if not any(patient["id"] == self.patient_id for patient in patients):
            print(f"Patient ID '{self.patient_id}' does not exist.")
            return None

        return {
            "patient_id": self.patient_id,
            "consultation": self.consultation_fee,
            "medicine": self.medicine_charge,
            "tests": self.test_charge,
            "room": self.room_charge,
            "discount": self.discount,
            "subtotal": self.subtotal(),
            "total": self.total(),
            "date": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def display_bill(self):

        bill = self.generate_bill()

        if bill is None:
            return False

        print("\nHospital Bill")
        print("=" * 40)

        for key, value in bill.items():
            print(f"{key.replace('_', ' ').title():<20}: {value}")

        print("=" * 40)

        return True