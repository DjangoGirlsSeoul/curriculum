#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
#If the score is between 0.0 and 1.0, print a grade using the following table:
#3.3 0.0부터 1.0 사이의 점수에 등급을 매기기 위한 프로그램을 작성하세요. 점수가 범위를 벗어난다면 에러 메세지를 프린트하세요.
#점수가 0.0부터 1.0 사이라면, 아래 테이블을 사용하여 등급을 프린트 해 보세요.
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.///
#유저가 범위를 벗어난 값을 입력하였다면, 적당한 에러 메세지가 프린트되고 종료되도록 하세요. 테스트를 위하여 점수를 0.85로 입력 해 보세요.


score = input("Please enter a score between 0.0 and 1.0:")
score.split()
"".join(score)
if score.isdigit():
    score = float(score)
    if score > 0.0 and score < 1.0:

        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
        print("Number not in range")
else:
    print("Not a Valid Number")
