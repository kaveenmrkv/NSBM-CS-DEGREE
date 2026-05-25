#question01-hotel billing system
RC_PD=int(input("Enter the Room charge per day Amount : "))
ND=int(input("Enter the Number of days that you are staying : "))
FC=int(input("Enter the Food charges amount : "))
SCP=int(input("Enter the service charge percentage :"))
Sub_Total=(RC_PD*ND)+FC
SC=Sub_Total*(SCP/100)
FullC=SC+Sub_Total
print("The Subtotal Bll amount excludig the service charge is  : ", Sub_Total, " LKR")
print("The Service charge is : ", SC, " LKR")
print("The Finale Bill Amount is : ", FullC, " LKR")
