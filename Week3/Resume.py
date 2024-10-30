Name = str(input("โปรดกรอกชื่อจริงของคุณ : "))
Age = int(input("โปรดกรอกอายุของคุณ : "))
Stu_ID = int(input("โปรดกรอกรหัสประจำตัวนักเรียนของคุณ : "))
Stu_Level = str(input("โปรดกรอกระดับชั้นของคุณ : "))
Nick_Name = str(input("โปรดกรอกชื่อเล่นของคุณ : "))
Height = float(input("โปรดกรอกส่วนสูงของคุณ : "))
Weight = float(input("โปรดกรอกน้ำหนักของคุณ : "))

print("ชื่อ: " + Name + " อายุ: " + str(Age) + " ปี\nรหัสประจำตัวนักเรียน: " + str(Stu_ID) + " ระดับชั้น: " + Stu_Level + "\nชื่อเล่น: " + Nick_Name + "\nส่วนสูง: " + str(Height) + " เซนติเมตร น้ำหนัก: " + str(Weight) + "กิโลกรัม\nส่วนสูง + น้ำหนัก = " + str(Height + Weight));