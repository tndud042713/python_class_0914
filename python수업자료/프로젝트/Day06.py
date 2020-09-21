import turtle as t

# 예제.1

# num1 = int(input(" 수 입력 : "))
# num2 = int(input(" 수 입력 : "))
# sum = num1+ num2
# if sum % 2 ==0:
#     if sum%3==0:
#         print("합은 짝수이며, 3의 배수입니다.")
#     else:
#         print("합은 짝수이지만, 3의 배수는 아닙니다.")
# else:
#     print("합은 짝수가 아닙니다.")

# 예제.2
# kor = int(input("국어점수 입력 : "))
# eng = int(input("영어점수 입력 : "))
# mat = int(input("수학점수 입력 : "))
# avg = (kor + eng + mat)/3
# if avg < 70:
#     print("평균점수 미달 불합격!!")
# elif kor <60:
#     print("국어점수 미달 불합격!!")
# elif eng <60:
#     print("영어점수 미달 불합격!!")
# elif mat <60:
#     print("수학점수 미달 불합격!!")
# else:
#     print("합격!!~")
# 위의 코드는 어떤 점수 미달로 떨어졌는지 상세하게 알려줄수 있는 장점이 있다.
#위의 프로그램은 과락 검사하는 프로그램이다.
#아래의 코드도 출력내용은 동일하다.
# kor = int(input("국어점수 입력 : "))
# eng = int(input("영어점수 입력 : "))
# mat = int(input("수학점수 입력 : "))
# avg = (kor + eng + mat)/3

# if (avg<70) or (kor<60) or (eng<60) or (mat<60):
#     print("불합격!!")
# else:
#     print("합격입니다!!~")

# pdf 문제 풀어보기(세개)

# 비만도 구하기 프로그램

# name=input("이름을 입력하시오 : ")
# h=float(input("키를 입력하시오 : "))
# w=float(input("체중을 입력하시오 : "))

# std = (h - 100) *0.9
# weight = w/std*100

# if weight<100:
#     print("저체중입니다.")
# elif weight>=100 and weight<110:
#     print("정상체중입니다.")
# elif weight>=110 and weight<120:
#     print("과체중입니다.")
# elif weight>=120 and weight<130:
#     print("비만입니다.")
# else:
#     print("고도비만입니다.")

# turtle을 이용한 조건을 가진 그림그리기

# n=int(input("몇각형 그리고싶어?? "))
# x=0;

# #t는 터틀의 약자

# if n>=3 and n<=10:
#     for x in range(n):
#         t.forward(100)
#         t.left(360/n)
#     t.mainloop()
# else:
#     print("도형을 그릴 수 없습니다")

# 윤년을 구하는 프로그램

# year = int(input("윤년을 판단하고 싶은 년도를 쓰시오 : "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("윤년입니다.")
#         else:
#             print("평년입니다.")
#     else:
#         print("윤년입니다.")
# else:
#     print("평년입니다.")

# quiz.1
# 사용자로부터 Gbyte의 값을 입력받아, byte,kbyte,Mbyte로 각각 출력되게 만드시오.
# (1.byte 2.kbyte 3.Mbyte)

# Gbyte = int(input("Gbyte값을 입력하시오 : "))
# option = int(input("출력하고 싶은 옵션을 선택하시오 1.byte 2.kbyte 3.Mbyte : "))
# byte=Gbyte*1024**3 #세제곱
# kbyte=Gbyte*1024**2 #제곱
# Mbyte=Gbyte*1024
# if option==1:
#     print("Gbyte를 byte로 변환한 값은 : {:.2f}byte 입니다.".format(byte))
# elif option==2:
#     print("Gbyte를 kbyte로 변환한 값은 : {:.2f}kbyte 입니다.".format(kbyte))
# elif option==3:
#     print("Gbyte를 Mbyte로 변환한 값은 : {:.2f}Mbyte 입니다.".format(Mbyte))
# else:
#     print("잘못입력")


# quiz.2
# 인증 프로그램을 만드시오.(ID: KGIDBANK, PW: P@$$w0rd)
# 1.아이디가 틀리면 등록되지 않은 아이디 입니다 출력
# 2.비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
# 3.아이디와 비밀번호가 일치한다면 인증 통과 출력

# ID = "KGIDBANK"
# PW = "P@$$w0rd"

# ID =input("아이디를 입력하시오 : ")
# PW =input("패스워드를 입력하시오 : ")

# if ID == "KGIDBANK":
#     if PW == "P@$$w0rd":
#         print("인증 통과")
#     else:
#         print("비밀번호가 틀렸습니다")
# else:
#     print("등록되지 않은 아이디 입니다")

# quiz.3
# name = input("이름을 입력하시오 : ")
# stnum = input("학번을 입력하시오 : ")
# kor=int(input("국어점수를 입력하시오 : "))
# eng=int(input("영어점수를 입력하시오 : "))
# mat=int(input("수학점수를 입력하시오 : "))
# avg=(kor+eng+mat)/3

# if avg>=90:
#     print(f"이름은 {name}이고 학번은{stnum}이고 평균은 {avg:.2f}이다 학점은 'A'이다.")
# elif avg>=80:
#     print(f"이름은 {name}이고 학번은{stnum}이고 평균은 {avg:.2f}이다 학점은 'B'이다.")
# elif avg>=70:
#     print(f"이름은 {name}이고 학번은{stnum}이고 평균은 {avg:.2f}이다 학점은 'C'이다.")
# elif avg>=60:
#     print(f"이름은 {name}이고 학번은{stnum}이고 평균은 {avg:.2f}이다 학점은 'D'이다.")
# else:
#     print(f"이름은 {name}이고 학번은{stnum}이고 평균은 {avg:.2f}이다 학점은 'F'이다.")

#quiz.4
coffee = int(input("사고싶은 커피의 개수를 입력하시오 : "))
if coffee>10:
    print("주문하신 가격은 {:,}원입니다.".format(2000*10+1500*(coffee-10)))
else:
    print("주문하신 가격은 {:,}원입니다.".format(2000*coffee))