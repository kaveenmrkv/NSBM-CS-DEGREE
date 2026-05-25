#Vehicle Trip Cost Estimator
#distance traveled
DT=float(input("Enter the Distance traveled in KMs : "))
#Fuel Efficiency
FE=float(input("Enter the Fuel Efficency (KMs that can be ran with 1 lite of fuel : "))
#Fuel Price Per litre
FPPL=float(input("Enter the Fuel price per litre : "))
#Highway Charges
HC=float(input("Enter the Highway Charges : "))
#Fuel Used
FU=DT/FE
print("The Amount of fuel is used is :", FU, "Litres")
#Fuel Cost
FC=FU*FPPL
print(" The Total Fuel Charge is : ",  FC , "  LKR")
FTC=FC+HC
print(" The Total Trip Cost is : ",  FTC , "  LKR")         
         
