#Student Scholarship Eligibility
#student Attendance
SA=float(input("Enter Student's Attendance Percentage : "))
AM=float(input("Enter Student's Average Mark : "))
if SA>=80 :
    if AM>=75:
        print("Scholarship Awarded")
    else:
        print("Scholarship NOT Awarded")
else:
    print("Insufficient Attendance")
