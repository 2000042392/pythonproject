class Hospital:
    def __init__(self):
        self.hos_name = input("Enter hospital name: ")
        self.hos_location = input("Enter hospital location: ")
        self.hos_phone = int(input("Enter hospital phone number: "))

    def display_hospitaldetails(self):
        print("Hospital Name:", self.hos_name)
        print("Hospital Location:", self.hos_location)
        print("Hospital Phone:", self.hos_phone)


class Department:
    def __init__(self):
        self.deptname = input("Enter department name: ")
        self.doctorname = input("Enter doctor name: ")

    def display_department(self):
        print("Department Name:", self.deptname)
        print("Doctor Name:", self.doctorname)


class Patient(Hospital, Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)

        self.patient_name = input("Enter patient name: ")
        self.age = int(input("Enter patient age: "))
        self.gender = input("Enter patient gender: ")
        self.phone = int(input("Enter patient phone number: "))
        self.admissiondate = input("Enter admission date: ")
        self.bedno = int(input("Enter bed number: "))
        self.dischargedate =""

    def set_discharge(self):
        self.dischargedate = input("Enter discharge date: ")

    def fullsummary(self):
        self.display_hospitaldetails()
        self.display_department()

        print("\nPatient Details")
        print("Patient Name:", self.patient_name)
        print("Patient Age:", self.age)
        print("Patient Gender:", self.gender)
        print("Patient Phone:", self.phone)
        print("Admission Date:", self.admissiondate)
        print("Bed No:", self.bedno)
        if self.dischargedate=="":
            print("not discharged")
        else:

         print("Discharge Date:", self.dischargedate)


p = Patient()
p.set_discharge()
p.fullsummary()






