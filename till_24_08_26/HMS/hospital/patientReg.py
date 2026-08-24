
patients = []


def register(id, name, age, gender, phone, on_spot_mentioned_problem):
    if id in patients:
        print(f"Patient ID {id} already exists.")
        return False

    patients[id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "on_spot_mentioned_problem": on_spot_mentioned_problem
    }
    return True


def display_id(id):
    if id not in patients:
        print(f"Patient ID {id} doesn't exist.")
        return False

    print(f"Details of Patient ID {id}:")
    for key, value in patients[id].items():
        print(f"  {key}: {value}")
    return True


def display_all():
    if not patients:
        print("No patients registered.")
        return False

    print("All Registered Patients:")
    for patient in patients:
        print(f"Patient ID: {patient}")
        for key, value in patients[patient].items():
            print(f"  {key}: {value}")
        print()
    return True
