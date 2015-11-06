#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use raw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.


#not checking errors: 

# hrs = input("Enter Hours:")
# pay = input("Enter Pay: ")
# hrs = float(hrs)
# pay = float(pay)
# if hrs <= 40:
# 	gross_pay = hrs*pay
# if hrs > 40:
# 	regular_pay = 40 * pay
# 	overtime_hours = hrs - 40
# 	overtime_pay = pay * 1.5
# 	overtime = overtime_hours * overtime_pay
# 	gross_pay = regular_pay + overtime
# print(gross_pay)



# checking input errors:

hrs = input("Enter Hours:")

if hrs.isdigit():
	pay = input("Enter Pay: ")
	numpay = pay.split(".")
	paystring = "".join(numpay)
	if paystring.isdigit():
		hrs = float(hrs)
		pay = float(pay)
		if hrs <= 40:
			gross_pay = hrs*pay
		if hrs > 40:
			regular_pay = 40 * pay
			overtime_hours = hrs - 40
			overtime_pay = pay * 1.5
			overtime = overtime_hours * overtime_pay
			gross_pay = regular_pay + overtime
		print(gross_pay)
	else: 
		print("Pay entered isn't a valid number.")
else: 
	print("Hours entered isn't a valid number.")