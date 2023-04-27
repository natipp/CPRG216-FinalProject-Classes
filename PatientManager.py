#Importing Patient class from Patient.py
from Patient import Patient

#Creation of the PatientManager class
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # Method to format the patient information for the file
    def format_patient_Info_for_file(self, patient):
        return f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"

    # Method to save the patient information to the file
    def enter_patient_info(self):
        pid = input("\nEnter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        patient = Patient(pid, name, disease, gender, age)

        return patient

    # Method to read the patient information from the file
    def read_patients_file(self):
        with open("Project Data\patients.txt", "r") as file:
            next(file)
            for line in file:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    # Method to search for a patient by their id
    def search_patient_by_Id(self):
        pid = input("\nEnter the Patient Id: ")

        for patient in self.patients:
            if patient.get_pid() == pid:
                self.display_patient_info(patient)
                return

        print("Can't find the Patient with the same id on the system")

    #Method to display the patient information
    def display_patient_info(self, patient):
        print(f"{'ID':<6}{'Name':<20}{'Disease':<15}{'Gender':<15}{'Age':<6}\n")
        print(f"{patient.get_pid():<6}{patient.get_name():<20}{patient.get_disease():<15}{patient.get_gender():<15}{patient.get_age():<6}")

    # Method to edir the patient information
    def edit_patient_info_by_id(self):
        patient_id = input(
            "\nPlease enter the id of the Patient that you want to edit their information: ")
        found_patient = None

        for patient in self.patients:
            if patient.get_pid() == patient_id:
                found_patient = patient
                break
        if found_patient:
            new_name = input("Enter new Name: ")
            new_disease = input("Enter new disease: ")
            new_gender = input("Enter new gender: ")
            new_age = input("Enter new age: ")

            found_patient.set_name(new_name)
            found_patient.set_disease(new_disease)
            found_patient.set_gender(new_gender)
            found_patient.set_age(new_age)

            with open("Project Data\patients.txt", "w") as file:
                for patient in self.patients:
                    file.write(
                        self.format_patient_Info_for_file(patient) + "\n")

            print(f"\nPatient whose ID is {patient_id} has been edited.")
        else:
            print(f"Cannot find the patient {patient_id}")

    #Method to display the list of patients
    def display_patients_list(self):
        print(f"{'ID':<6}{'Name':<20}{'Disease':<15}{'Gender':<15}{'Age':<6}\n")
        for patient in self.patients:
            print(f"{patient.get_pid():<6}{patient.get_name():<20}{patient.get_disease():<15}{patient.get_gender():<15}{patient.get_age():<6}\n")

    # Method to write the list of patients to the file
    def write_list_of_patients_to_file(self):
        with open("Project Data\patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_Info_for_file(patient) + "\n")

    #Method to add a patient to the list
    def add_patient_to_file(self):
        # Ask user to enter patient info
        new_patient = self.enter_patient_info()

        # Add patient to the list
        self.patients.append(new_patient)

        # Add patient to the file
        with open("Project Data\patients.txt", "a") as file:
            file.write(self.format_patient_Info_for_file(new_patient))

        print(f"\nPatient whose ID is {new_patient.get_pid()} has been added.")
