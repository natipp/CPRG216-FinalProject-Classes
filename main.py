# Description:      This program lets you manage a list of Doctors and Patients. There are 5 classes. Doctor, DoctorManager, Patient,
#                   PatientManager, and Managerment. The Manager classes import their non-manager counterparts and Management imports
#                   the managers.
#
# Team Members:     Nathalia P., Anna R., Jubril S.
#
# Date:             April 26th, 2023
#
# Inputs:           The user will have many different menus that they can navigate through in order to obtain the information that
#                   they desire. As such, the inputs are the 2 txt file in the 'Project Data' folder and user input.
#
# Outputs:          THe output will be whatever information the user is requesting from the program, this could be a list of doctors,
#                   information about a patient, etc. It also updates the 2 txt files in the 'Project Data' folder


import Management

# Instantiate a Management object
management = Management.Management()

# Call the display_menu() method
management.display_menu()
