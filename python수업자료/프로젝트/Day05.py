# 예제.1

# print(3 & 5)
# print(3 | 5)
# print(3 ^ 5)
# print(5 << 2)
# print(5 >> 2)

# [ IF문 사용하기 ]
# : 조건식이 참일 경우 종속문장을 실행
# : 참이 아닐 경우 IF문 종료 
# : IF문은 중첩적으로 사용 가능
# : IF문의 수행코드를 작성 할 때에는 반드시 들여쓰기를 해야 한다.

#[예제.1]
# num = int(input("정수 입력: "))
# if num % 2==0:
#     print("num변수의 값은 짝수")
#     print("num변수의 값은 2의 배수")
# print("프로그램 종료!")

# 예제.2
# print("1.Easy Game Strat")
# print("2.Hard Game Strat")
# print("1.Game Exit")
# num = int(input("번호 선택 >> "))
# if num == 1:
#     print("쉬움 모드 실행!")
# if num == 2:
#     print("어려움 모드 실행!")
# if num == 3:
#     print("게임 종료!")

# 예제.3
# x=15
# if x>0:
#     print("x변수의 값은 0보다 크다")
# if x<10:
#     print("x변수의 값은 10보다 작다")

# 예제.
# su=int(input("데이터 입력: "))
# if su in(1,2,3,4,5,6,7,8,9,10):
#     print("입력하신 데이터는 데이터 그룹에 속해있습니다")

# su2 = int(input("데이터 입력: "))
# if su2 not in (1,2,3,4,5,6,7,8,9,10):
#     print("입력하신 데이터는 데이터 그룹에 속해있지 않습니다.")

# 예제.5
# su3 =100
# if type(su3) is int:
#     print("su3 자료형은 int형 자료형입니다.")

# 예제.6

# if True:
#     print("참")
# if False:
#     print("거짓")
# if 1:
#     print("참")
# if 0:
#     print("거짓")

# num = int(input("정수입력: "))
# if num % 5:
#     print("테스트")

# [Quiz]
# 날짜를 입력 받아 요일을 구하시오.
# (단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일)
# (어떤 값을 입력을 받던 요일이 정확히 출력 되게 만드시오)

# day = int(input("날짜입력: "))
# ret = day%7
# if ret == 1: print(day,": 월요일")
# if ret == 2: print(day,": 화요일")
# if ret == 3: print(day,": 수요일")
# if ret == 4: print(day,": 목요일")
# if ret == 5: print(day,": 금요일")
# if ret == 6: print(day,": 토요일")
# if ret == 0: print(day,": 일요일")

#[예제.7]
# su = int(input("수 입력: "))
# if su >= 10 and su <=20:
#     print("입력하신 수의 범위는 10 ~ 20사이 입니다.")
# if su == 10 or su == 20:
#     print("입력하신 수는 10이거나, 20입니다.")

# 예제.8
# num = int(input("정수입력 : "))
# if num ==100:
#     print("num변수의 값은 100 입니다.")
# else:
#     print("num변수의 값은 100이 아닙니다.")

# [ IF문제 ]
# 1. 입력한 데이터가 3의 배수인 경우 출력하시오.
# 2. 절대값을 구하는 프로그램을 작성하시오.
# 3. 수를 입력 받아 짝,홀수를 구분하여 출력하시오.
# 4. 두수를 입력 받아 큰 수를 출력하시오.
# 5. 세수를 입력 받아 큰 수를 출력하시오.
# 6. 두수를 입력 받아 큰 수가 짝수이면 출력하시오.
# 7. 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.

#3의 배수
# su = int(input("수 입력: "))
# if su%3==0:
#     print("3의 배수입니다.")
# else:
#     print("3의 배수가 아닙니다.")

# 절대값을 구하는 프로그램

# su = int(input("수 입력: "))
# if su<0:
#     print(-su)
# else:
#     print(su)

# 짝홀을 구분하는 프로그램
# su = int(input("수 입력: "))
# if su%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# 두수를 입력 받아 큰 수를 출력하시오
# su1 = int(input("첫번째 수 입력 : "))
# su2 = int(input("두번째 수 입력 : "))
# if su1>su2:
#     print(su1)
# else:
#     print(su2)

# su1 = int(input("첫번째 수 입력 : "))
# su2 = int(input("두번째 수 입력 : "))
# su3 = int(input("세번째 수 입력 : "))

# if su1>su2 and su1>su3:
#     print(su1)
# elif su2>su1 and su2>su3:
#     print(su2)
# elif su3>su1 and su3>su2:
#     print(su2)

# 두수를 입력 받아 큰 수가 짝수이면 출력하시오

# su1 = int(input("첫번째 수 입력 : "))
# su2 = int(input("두번째 수 입력 : "))
# if su1>su2 and su1%2==0:
#     print(su1,"은",su2,"보다 크면서 짝수이다")
# if su2>su1 and su2%2==0:
#     print(su2,"은",su1,"보다 크면서 짝수이다")

# 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력

# su1 = int(input("첫번째 수 입력 : "))
# su2 = int(input("두번째 수 입력 : "))
# sum=su1+su2
# if sum%2==0 and sum%3==0:
#     print("두 수의 합",sum,"은 짝수이고, 3의 배수이다.")
