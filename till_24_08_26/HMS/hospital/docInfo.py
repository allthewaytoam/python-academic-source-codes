doctors = ()


def add_doc(did, name, spec):
    global doctors

    if any(doctor[0] == did for doctor in doctors):
        print(f"Doctor ID '{did}' already exists.")
        return False

    if not did or not name or not spec:
        print("All doctor details are required.")
        return False

    doctors += ((did, name.strip().title(), spec.strip().title()),)

    print(f"Doctor ID '{did}' added successfully.")
    return True


def rem_doc(did):
    global doctors

    if not any(doctor[0] == did for doctor in doctors):
        print(f"Doctor ID '{did}' does not exist.")
        return False

    doctors = tuple(doctor for doctor in doctors if doctor[0] != did)

    print(f"Doctor ID '{did}' removed successfully.")
    return True


def disp_doc(did):
    for doctor in doctors:
        if doctor[0] == did:
            print("\nDoctor Details")
            print("-" * 30)
            print(f"Doctor ID: {doctor[0]}")
            print(f"Name: {doctor[1]}")
            print(f"Specialization: {doctor[2]}")
            return True

    print(f"Doctor ID '{did}' does not exist.")
    return False


def disp_all_doc():
    if not doctors:
        print("No doctors registered.")
        return False

    print("\nAll Registered Doctors\n")

    for did, name, spec in doctors:
        print(
            f"ID: {did} | "
            f"Name: {name} | "
            f"Specialization: {spec}"
        )

    return True