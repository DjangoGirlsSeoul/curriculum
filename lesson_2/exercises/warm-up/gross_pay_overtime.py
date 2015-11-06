#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# 40시간 이상 일할 경우, 시급을 1.5배로 종업원에게 지급하는 급여 계산 프로그램을 input을 사용하여 작성하세요.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#45시간의 근무시간과 10.50의 시급을 테스트를 위하여 사용하세요. (총급여는 498.75가 되어야 합니다.)
#You should use input to read a string and float() to convert the string to a number.
#string을 읽어내는데는 input을, string을 숫자로 변환시키는데는 float()를 사용해야 합니다.
#Do not worry about error checking the user input - assume the user types numbers properly.
#에러 확인에 신경쓰지 않아도 됩니다. 사용자가 입력하는 값들은 정확하다고 간주하세요.

hrs = raw_input("Enter Hours:")
h = float(hrs)
