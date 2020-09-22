'''
[Quiz.5]
정수를 입력받아 아래와 같이 출력하시오.
3의배수이면서, 4의배수입니다. 
3의배수 입니다.
4의배수 입니다.
3의배수도, 4의배수도 아닙니다. 
0은 3의 배수도 4의 배수도 아닙니다.

[Quiz.6] : [ EX (31분 ~ 40분: 35000, 41분 ~ 50분: 40000 ) ]
비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 
10분 단위로 추가요금 5000원씩 부가된다. 
비행기 탈 시간을 입력하여 요금 계산기를 만드시오.

# [Quiz.5]
num = int(input('정수 입력 : '))
if num == 0:
    print(num,"은(는) 3의 배수도 4의 배수도 아닙니다");
elif num % 3 == 0 and num % 4 == 0:
    print(num,"은(는)3의 배수 이면서,4의 배수입니다");
elif num % 3 == 0:
    print(num,"은(는)3의 배수 입니다");
elif num % 4 == 0:
    print(num,"은(는)4의 배수 입니다");
else:
    print(num,"는 3의 배수도 4의 배수도 아님");

# [Quiz.6]
money=30000
time = int(input("비행기 탄 시간(분): "))
time -= 30 # time = time - 30
if time > 0:
    money += (5000+((time-1)//10)*5000)
    #if (time % 10) == 0:
    #    money=money+time//10*5000
    #else:
    #    money = money + time // 10 * 5000 + 5000
print(money,"원 입니다.")

# [예제.1]
for i in range(0,10,1):
    print("TEST")

# [예제.2]
for i in range(10,0,-1):
    print("TEST")

# [예제.3]
for i in range(0,10,2):
    print("TEST")

# [예제.4] 
# : range 함수는 시작값, 증가값을 지정하지 않을 
#  경우 시작값은 0, 증가값 1로 설정하여 동작한다.

for i in range(10):
    print(i, end='\t')
print()
print("TEST")
print("TEST")

# [예제.5] 
for i in range(5,10):
    print(i, end='\t')
print()
print("TEST")
print("TEST")

# [예제.6] 
Sum = 0
start, end, grow = 0, 0, 0

start = int(input("시작 값 입력: "))
end = int(input("종료 값 입력: "))
grow = int(input("증가 값 입력: "))

for x in range(start,end+1,grow):
    Sum += x
print("{}에서 {}까지 {}씩 증가한 누적합: {}".format(start,end,grow,Sum))

# [예제.7] : Range() 함수 사용 안 함
for v in "Test String":
    print(v)

S = "Python"
for v2 in S:
    print(v2,end=" ")
'''










