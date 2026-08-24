from hospital import appointmentScheduling, billingSystem, docInfo, medRecStorage, patientReg, reportGen

def reg_patient():
    id = str(input("Enter Patient ID: "))
    name = str(input("Enter Patient Name: "))
    age = int(input("Enter Patient Age: "))
    gender = str(input("Enter Patient Gender: "))
    phone = str(input("Enter Patient Phone Number: "))
    on_spot_mentioned_problem = str(input("Enter On-Spot Mentioned Problem: "))
    status = patientReg.register(id, name, age, gender, phone,on_spot_mentioned_problem)
    print(f"Patient Registration Status: {'Success' if status else 'Failed'}")


def menu():
    looper = True
    space = True
    while looper:
        print("Menu:\n1: Register a patient\n2: Display details of a patient\n3: Display details of every existing patients\n10: Exit")
        chc = int(input("Enter your choice: "))
        print()
        match chc:
            case 1:
                reg_patient()
            case 2:
                id = str(input("Enter Patient ID: "))
                patientReg.display_id(id)
            case 3:
                patientReg.display_all()
            case 10:
                looper = False
            case _:
                print("\t--\u00b7 Invalid choice. Please try again \u00b7--\n\nRe opeing the ", end="")
                space=False
        if space:
            print("")
    print("\t===============================\n\t|| Thank you for using AMHMS ||\n\t===============================\n")


def welcome():
    print("\t========================================\n\t|| AMHMS \u00b7 Hospital Management System ||\n\t========================================\n\n")


def main():
    welcome()
    menu()

if __name__ == "__main__":
    main()