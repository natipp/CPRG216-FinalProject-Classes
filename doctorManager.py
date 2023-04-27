class doctorManager:
    def __init__(self, doctors):
        self.doctors = []
        self.read_doctorss_file()

    def format_dr_info(self):
        return f"{self.id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

    def enter_dr_info(self):
        id = input('Please enter the doctor id:')
        name = input("Please enter the doctor's name:")
        specialization = input("Please enter the doctor's specialization:")
        working_time = input("Please enter the doctor's working time:")
        qualification = input("Please enter the doctor's qualification:")
        room_number = int(input("Please enter the doctor's room number:"))
        doctor = doctor(id, name, specialization, working_time, qualification,room_number)
        return doctor
    
    def search_doctor_by_id(self):
        id2 = input("Please enter the doctor id: ")
        for dr in self.doctors:
            if doctor.get_id() == id2:
                print(doctorManager.format_dr_info())
            else:     
                print("Can't find the doctor with the same ID on the system.")

    def search_doctor_by_name(self):
        name2 = input("Please enter the doctor's name: ")
        for dr in self.doctors:
            if doctor.get_name() == name2:
                print(doctorManager.format_dr_info())
            else:     
                print("Can't find the doctor with the same name on the system.")

    def display_doctor_info(self):
    
     def edit_doctor_info(self):
        id3 = input('Please enter the id of the doctor that you want to edit their information:')
        for dr in self.doctors:
            if doctor.get_id() == id3:
                new_name = input("Enter new Name: ")
                new_specilist = input("Enter new Specilist in: ")
                new_working_time = input("Enter new Timing: ")
                new_qualification = input("Enter new Qualification: ")
                new_room_number = input("Enter new Room number: ")

            else:
                print(f"Cannot find the doctor {id3}")

    def display_doctors_lists(self):
        print self.doctors

    def write_list_of_doctors_to_file(self):

    def add_dr_to_file(self):
        