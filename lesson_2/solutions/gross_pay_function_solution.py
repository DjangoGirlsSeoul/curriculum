#4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of time-and-a-half in a function called computepay()
#and use the function to do the computation.
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use raw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input.
#Challenge: check the user input for errors
# 40시간 이상 일할 경우, 시급을 1.5배로 종업원에게 지급하는 급여 계산 프로그램을 input을 사용하여 작성하세요.
#근무 시간과 시급을 매개 변수로 갖는 함수 computepay()를 사용하여, 초과근무에 대해서는 50%의 초과 근무수당을 계산하도록 하세요.
#함수는 값으로 나와야 합니다. 24시간의 근무시간과 10.50의 시급을 테스트를 위하여 사용해 보세요. (총급여는 498.75가 되어야 합니다.)
#string을 읽어내는데는 input을, string을 숫자로 변환시키는데는 float()를 사용해야 합니다.
#에러 확인에 신경쓰지 않아도 됩니다. 사용자가 입력하는 값들은 정확하다고 간주하세요.

#도전해보기: 유효한 숫자임을 확인하는 코드를 작성 해 보세요.


def computepay(hrs, pay):
	hrs = float(hrs)
	pay = float(pay)
	if hrs <= 40:
		gross_pay = hrs * pay
	if hrs > 40:
		regular_pay = 40 * pay
		overtime_hours = hrs - 40
		overtime_pay = pay * 1.5
		overtime = overtime_hours * overtime_pay
		gross_pay = regular_pay + overtime
		return(gross_pay)

print(computepay(input("Enter Hours:"), input("Enter Pay: ")))



#checking for input errors:


# def computepay(hrs, pay):
# 	if hrs.isdigit():
# 		numpay = pay.split(".")
# 		paystring = "".join(numpay)
# 		if paystring.isdigit():
# 			hrs = float(hrs)
# 			pay = float(pay)
# 			if hrs <= 40:
# 				gross_pay = hrs*pay
# 			if hrs > 40:
# 				regular_pay = 40 * pay
# 				overtime_hours = hrs - 40
# 				overtime_pay = pay * 1.5
# 				overtime = overtime_hours * overtime_pay
# 				gross_pay = regular_pay + overtime
# 			return(gross_pay)
# 		else:
# 			return("Pay entered isn't a valid number.")
# 	else:
# 		return("Hours enter isn't a valid number.")

# print(computepay(input("Enter Hours:"), input("Enter Pay: ")))
