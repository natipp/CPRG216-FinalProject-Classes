from DoctorManager import DoctorManager
from PatientManager import PatientManager

# Instanciate the DoctorManager and PatientManager classes
dr_manager = DoctorManager()
pt_manager = PatientManager()


class Management:
    def __init__(self):
        self.doctors = []
        self.patients = []

    def display_menu(self):
        while True:
            # Display initial menu options
            print("Welcome to Alberta Hospital (AH) Managment system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - 	Doctors")
            print("2 - 	Patients")
            print("3 -	Exit Program")
            choice = input(">>> ")

            # Handle user input
            if choice == "1":
                self.doctors_menu()
            elif choice == "2":
                self.patients_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def doctors_menu(self):
        while True:
            # Display doctors menu options
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input(">>> ")

            # Handle user input
            if choice == "1":
                dr_manager.display_doctors_list()
            elif choice == "2":
                dr_manager.search_doctor_by_id()
            elif choice == "3":
                dr_manager.search_doctor_by_name()
            elif choice == "4":
                dr_manager.add_dr_to_file()
            elif choice == "5":
                dr_manager.edit_doctor_info()
            elif choice == "6":
                print()
                break
            else:
                print("Invalid choice. Please try again.")

    def patients_menu(self):
        while True:
            # Display patients menu options
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>> ")

            # Handle user input
            if choice == "1":
                pt_manager.display_patients_list()
            elif choice == "2":
                pt_manager.search_patient_by_Id()
            elif choice == "3":
                pt_manager.add_patient_to_file()
            elif choice == "4":
                pt_manager.edit_patient_info_by_id()
            elif choice == "5":
                print()
                break
            else:
                print("Invalid choice. Please try again.")
