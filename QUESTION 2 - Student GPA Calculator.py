#GPA Calculator
M1=float(input("Enter your marks for the subject 01 : "))
M2=float(input("Enter your marks for the subject 02 : "))
M3=float(input("Enter your marks for the subject 03 : "))
M4=float(input("Enter your marks for the subject 04 : "))
ST=M1+M2+M3+M4
AVG=(ST/4)
GPA=(AVG/25)
print("The subtotal is :", ST)
print("The Average is :", AVG)
print("The GPA is :", GPA)
