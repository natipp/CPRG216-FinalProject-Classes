import Patient
class PatientManager:
    def __init__(self, patients):
        self.patients = []
        self.read_patients_file()

    def format_patient_Info_for_file(self, patient):
        return f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"

    def enter_patient_ilnfo(self):
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        patient = Patient(pid, name, disease, gender, age)
        return patient
    
    def read_patients_file(self):
        with open("Project Data\patients.txt", "r") as file:
            next(file)
            for line in file:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)
    
    def search_patient_by_Id(self):
        found_patient = False
        pid = input("Enter the Patient Id: ")
        for patient in self.patients:
            if patient.get_pid() == pid:
                found_patient = True
                print(patient.format_patient_Info_for_file())
                break
        if not found_patient:         
            print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        print("ID     Name          Disease       Gender     Age")
        print(f"{patient.get_pid()}     {patient.get_name()}         {patient.get_disease()}       {patient.get_gender()}       {patient.get_age()}")

    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
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
                    file.write(self.format_patient_Info_for_file(patient) + "\n")
                
            print(f"Patient whose ID is {patient_id} has been edited.")
        else:
            print(f"Cannot find the patient {patient_id}")
    
    def display_patients_list(self):
        print(f"{'ID':<6}{'Name':<20}{'Disease':<15}{'Gender':<15}{'Age':<6}")
        for patient in self.patients:
            print(f"{patient.get_pid():<6}{patient.get_name():<20}{patient.get_disease():<15}{patient.get_gender():<15}{patient.get_age():<6}")

    def write_list_of_patients_to_file(self):
        with open("Project Data\patients.txt", "w") as file:
            for patient in self.patients:
                    file.write(self.format_patient_Info_for_file(patient) + "\n")

    def add_patient_to_file(Self):
        new_patient = Self.enter_patient_ilnfo()
        Self.patients.append(new_patient)
        new_patient_info = Self.format_patient_Info_for_file(new_patient)
        with open("Project Data\patients.txt", "a") as file:
            file.write("\n" + new_patient_info)
        print(f"Patient whose ID is {new_patient.get_pid()} has been added.")
