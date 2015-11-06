#2.3 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
#You should use raw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking or bad user data.

# This first line is provided for you

#not checking for errors:

hrs = input("Enter Hours:")
pay = input("Enter Pay:")
hrs = float(hrs)
pay = float(pay)
gross_pay = hrs*pay
print(gross_pay)
	




#checking input for errors

# hrs = input("Enter Hours:")
# if hrs.isdigit():
# 	pay = input("Enter Pay: ")
# 	numpay = pay.split(".")
# 	paystring = "".join(numpay)
# 	if paystring.isdigit():
# 		hrs = float(hrs)
# 		pay = float(pay)
# 		gross_pay = hrs*pay
# 		print(gross_pay)
# 	else: 
# 		print("Pay isn't a valid number.")
# else: 
# 	print("Hours isn't a valid number.")
