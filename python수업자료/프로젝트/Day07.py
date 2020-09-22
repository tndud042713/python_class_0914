import math

# # 퀴즈.5
# # 정수를 입력받아 아래와 같이 출력사히오.
# # 3의 배수이면서, 4의 배수입니다.
# # 3의 배수입니다.
# # 4의 배수입니다.
# # 3의 배수도, 4의 배수도 아닙니다.
# su = int(input("정수를 입력하시오 : "))
# if su%3 == 0:
#     if su%4 == 0:
#         print("3의 배수이면서, 4의 배수입니다.")
#     else:
#         print("3의 배수입니다.")
# else:
#     if su%4 == 0:
#         print("4의 배수입니다.")
#     else:
#         print("3의 배수도, 4의 배수도 아닙니다.")

# # 퀴즈.6 [EX (31분~40분 : 35000원, 41분 ~ 50분: 40000원)]
# # 비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며,
# # 10분 단위로 추가요금 5000원이 부가된다.
# # 비행기 탈 시간을 입력하여 요금 계산기를 만드시오.

# #발상이 떠오르지 않아서 math를 import해서 ceil 함수를 이용
# time = int(input("비행기 탈 시간(분단위)을 입력하시오 : "))
# basic_fare = 30000
# n= math.ceil((time-30)/10)
# fare = 5000
# if time>30:
#     print("요금은",30000+n*fare,"원 입니다!!")    
# else:
#     print("요금은",30000,"원 입니다!!")

# # 강사님 풀이
# money = 30000
# time = int(input("비행기 탄 시간(분): "))
# time = time - 30
# if time > 0:
#     money += (5000+((time-1)//10)*5000)
#     # if(time%10)==0:
#     #     money = money + time//10*5000
#     # else:
#     #     money = money + time//10*5000+5000
# print(money,"원 입니다.")

# 강사님풀이와 내 풀이 비교
# 일단 나는 발상을 못떠올렸고
# 1~10 이렇게 되는 값의 처리를 떠올리지 못했다.
# "//"연산자를 떠올리지 못했음
# 그래서 math.ceil 처럼 진도를 넘어선 함수를 이용하려고 했다.
# 풀이보고 다시한번 프로그램 짜보기 

# 반복문
# 예제.1
# for i in range(0,10,1):
#     print("TEST")

# 예제.2
# for i in range(10,0,-1):
#     print("TEST")

# 예제.3
# for i in range(0,10,2):
#     print("TEST")

# 예제.4
# : rangew 함수는 시작값, 증가값을 지정하지 않을
# 경우 시작값은 0, 증가값 1로 설정하여 동작한다.
# for i in range(10):
#     print(i,end='\t')
# print()
# print("TEST")
# print("TEST")

# 반복문을 쓰다보면 같은 줄에 출력하고 싶은 경우가 생김~~
# 이럴땐 end 함수를 이용한다.

# 예제.5
# 5부터 시작해서 종료값 10, 값은 1씩 증가
# for i in range(5,10):
#     print(i,end='\t')
# print()
# print("TEST")
# print("TEST")

# 예제.6
# i, Sum = 0,0
# start, end, grow = 0,0,0
# start = int(input("시작 값 입력 : "))
# end = int(input("종료 값 입력 : "))
# grow = int(input("증가 값 입력 : "))

# for x in range(start,end+1,grow):
#     Sum+=x
# print("{}에서 {}까지 {}씩 증가한 누적합: {}".format(start,end,grow,Sum))

# 예제.7
#range를 사용하지 않는 경우
# for v in "TEST String":
#     print(v)

# S="python"
# for v2 in S:
#     print(v2,end=" ")

