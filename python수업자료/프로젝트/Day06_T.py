'''
# [예제.1]
num1 = int(input('수 입력 : '))
num2 = int(input('수 입력 : '))
Sum = num1+num2
if Sum % 2 == 0 and Sum % 3 == 0:
    print('두수의 합은 짝수이며 3의 배수이다')
else:
    print("두수의 합은 짝수가 아니거나, 3의 배수가 아닙니다.")

num1 = int(input('수 입력 : '))
num2 = int(input('수 입력 : '))
Sum = num1+num2
if Sum % 2 == 0:
    if Sum % 3 == 0:
        print("합은 짝수이며, 3의 배수입니다.")
    else:
        print("합은 짝수이지만, 3의 배수는 아닙니다.")
else:
    print("합은 짝수가 아닙니다.")

# [예제.2]
kor = int(input("국어점수 입력: "))
eng = int(input("영어점수 입력: "))
mat = int(input("수학점수 입력: "))
avg = (kor + eng + mat) / 3
if (avg < 70) or (kor < 60) or (eng < 60) or (mat < 60): 
    print("불합격!!!")
else:
    print("합격!!!")

kor = int(input("국어점수 입력: "))
eng = int(input("영어점수 입력: "))
mat = int(input("수학점수 입력: "))
avg = (kor + eng + mat) / 3
if avg < 70:
    print("평균점수 미달 불합격!!!")
elif kor < 60:
    print("국어점수 미달 불합격!!!")
elif eng < 60:
    print("영어점수 미달 불합격!!!")
elif mat < 60:
    print("수학점수 미달 불합격!!!")
else:
    print("합격!!!")

#[문제.1]
print("### 정보입력 ###")
name = input("이름입력: ")
k = float(input("신장입력: "))
w = float(input("체중입력: "))
s = (k-100) * 0.9
b = w / s * 100

if b < 100:
    STR = "저 체중"
elif b >= 100 and b < 110:
    STR = "정상 체중"
elif b >= 110 and b < 120:
    STR = "과 체중"
elif b >= 120 and b < 130:
    STR = "비만"
else:
    STR = "고도비만"
print("{}님의 비만도는 {:.2f}%로 {} 입니다.".format(name,b,STR))

#[문제.2]
import turtle
num = int(input("3 ~ 10사이 정수입력: "))
if num == 3:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 4:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 5:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 6:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 7:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 8:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 9:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 10:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)    
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()    
else:
    print("그릴 수 없습니다.")

#[문제.3]
year = int(input("년도를 입력하세요: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"년도는 윤년입니다.")
        else:
            print(year,"년도는 평년입니다.")
    else:
        print(year,"년도는 윤년입니다.")
else:
    print(year,"년도는 평년입니다.")

[Quiz.1]
사용자로 부터 Gbyte의 값을 입력받아 byte,Kbyte,Mbyte로 각각 출력 되게 만드시오.
(1.byte 2.Kbyte 3.Mbyte 선택)

[Quiz.2] 
인증 프로그램을 만드시오. (ID: KGITBANK, PW: P@$$w0rd)
1.아이디가 틀리면 등록되지 않은 아이디 입니다 출력
2.비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
3.아이디와 비밀번호가 일치한다면 인증 통과 출력

ID = "KGITBANK"
PW = "P@$$w0rd"

# [Quiz.1]
GB = int(input("GByte 입력: "))
num = int(input("1.Byte 2.KByte 3.MByte >> "))
if num == 1:
    print("GByte : {} --> {}Byte".format(GB,GB*1024**3))
elif num == 2:
    print("GByte : {} --> {}KByte".format(GB,GB*1024**2))
elif num == 3:
    print("GByte : {} --> {}MByte".format(GB,GB*1024))
else:
    print("잘 못 입력!")

# [Quiz.2]
ID = "KGITBANK"
PW = "P@$$w0rd"
print("## 인증프로그램 시작 ##")
new_ID = input("ID 입력: ")
new_PW = input("PW 입력: ")
if new_ID == ID:
    if new_PW == PW:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다")
else:
    print("등록되지 않은 ID입니다")

[Quiz.3]
이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 
평균이 90이상이면 'A', 80 이상 'B', 70이상 'C', 60이상 'D', 60미만이면 'F'를 출력하시오

[Quiz.4]
커피의 개당 가격은 2000원이다. 
10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다. 
커피의 개수를 입력 받아 금액을 출력하시오.

# [Quiz.3]
name = input("이름입력: ")
h = input("학번입력: ")
kor = int(input("국어점수: "))
eng = int(input("영어점수: "))
mat = int(input("수학점수: "))
Sum = kor + eng + mat
avg = Sum / 3
grade = ''
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'
print("============== 학생정보 ==============")
print("학생이름: {}\t학번: {}".format(name,h))
print("국어: {}, 영어: {}, 수학: {}, 총점: {}, 평균: {:.2f}, 등급: {}".format(kor,eng,mat,Sum,avg,grade))

# [Quiz.4]
money = 0
num = int(input("커피 몇 잔? "))
if num > 10:
    #money = money + 20000 + (num - 10) * 1500
    money += 20000 + (num - 10) * 1500
elif num > 0 and num <= 10:
    money = num * 2000
print("총 가격: {:,}원 입니다.".format(money))

'''











