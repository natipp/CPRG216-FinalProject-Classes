from Doctor import Doctor


class DoctorManager:
    # Constructor
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, dr):
        return f"{dr.get_doctor_id()}_{dr.get_name()}_{dr.get_specialization()}_{dr.get_working_time()}_{dr.get_qualification()}_{dr.get_room_number()}"

    def enter_dr_info(self):
        dr_id = input("\nEnter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specility: ")
        working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")

        print(f"\nDoctor whose ID is {dr_id} has been added")

        return Doctor(doctor_id=dr_id, name=name, specialization=specialization,
                      working_time=working_time, qualification=qualification, room_number=room_number)

    def read_doctors_file(self):
        with open("Project Data\doctors.txt", "r") as f:
            for line in f:
                dr_info = line.strip().split("_")
                dr = Doctor(doctor_id=dr_info[0], name=dr_info[1], specialization=dr_info[2],
                            working_time=dr_info[3], qualification=dr_info[4], room_number=dr_info[5])
                self.doctors.append(dr)

    def search_doctor_by_id(self):
        dr_id = input("\nEnter the doctor Id: ")
        for dr in self.doctors:
            if dr.get_doctor_id() == dr_id:
                self.display_doctor_info(dr)
                return

        print(f"Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        name = input("\nEnter the doctor name: ")
        for dr in self.doctors:
            if dr.get_name() == name:
                self.display_doctor_info(dr)
                return
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, dr):
        print(
            f"\n{'ID':<6}{'Name':<20}{'Speciality':<15}{'Timing':<15}{'Qualification':<15}{'Room Number':<11}")
        print(f"\n{dr.get_doctor_id():<6}{dr.get_name():<20}{dr.get_specialization():<15}{dr.get_working_time():<15}{dr.get_qualification():<15}{dr.get_room_number():<11}")

    def edit_doctor_info(self):
        # Ask the user to enter the doctor id
        doctor_id = input(
            "\nPlease enter the id of the doctor that you want to edit their information: ")

        # Search for the doctor in the list of doctors
        found_doctor = False

        for dr in self.doctors:
            if dr.get_doctor_id() == doctor_id:
                found_doctor = True

                # Ask the user to enter the new information
                new_name = input("Enter new Name: ")
                new_specialization = input("Enter new Specilist in: ")
                new_timing = input("Enter new Timing: ")
                new_qualification = input("Enter new Qualification: ")
                new_room_number = input("Enter new Room number: ")

                # Update the doctor's information
                dr.set_name(new_name)
                dr.set_specialization(new_specialization)
                dr.set_working_time(new_timing)
                dr.set_qualification(new_qualification)
                dr.set_room_number(new_room_number)

                # Update doctors.txt
                self.write_list_of_doctors_to_file()

                print(f"\nDoctor whose ID is 66 has been edited")

        # If the doctor does not exist, display an error message
        if not found_doctor:
            print(f"Can't find the doctor with the same ID on the system")

    def display_doctors_list(self):
        print(f"{'ID':<6}{'Name':<20}{'Speciality':<15}{'Timing':<15}{'Qualification':<15}{'Room Number':<11}")
        for dr in self.doctors:
            print(f"\n{dr.get_doctor_id():<6}{dr.get_name():<20}{dr.get_specialization():<15}{dr.get_working_time():<15}{dr.get_qualification():<15}{dr.get_room_number():<11}")

    def write_list_of_doctors_to_file(self):
        with open("Project Data\doctors.txt", "w") as f:
            for dr in self.doctors:
                f.write(self.format_dr_info(dr) + "\n")

    def add_dr_to_file(self):
        # Ask the user to enter the doctor's information
        new_dr = self.enter_dr_info()

        # Add the doctor to the list of doctors
        self.doctors.append(new_dr)

        # Add the doctor to doctors.txt
        with open("Project Data\doctors.txt", "a") as f:
            f.write(self.format_dr_info(new_dr) + "\n")
