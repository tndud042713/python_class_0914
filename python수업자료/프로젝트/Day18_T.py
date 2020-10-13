'''
# [예제.1]
def func1(a):
    if a == 1:
        return
        print("함수실행")
func1(1)
print("프로그램 실행종료")    

# [예제.2]
def func2():
    print("함수실행")
    a = input("리턴값 입력: ")
    return a
ret = func2()
print("리턴값 출력:", ret)

# [예제.3]
def calc(su1,su2):
    ret = su1 + su2
    print("계산기실행")
    return ret
su1,su2 = int(input("정수입력: ")), int(input("정수입력: "))
result = calc(su1, su2)
print(su1,"+",su2,"=",result)

# [예제.4]
def sum_func(*par):
    print(par,type(par))
    result = 0
    for i in par:
        result += i
    return result
Sum = sum_func(10,20)
print("첫 번째 결과 출력:", Sum)
Sum = sum_func(10,20,30,40,50)
print("두 번째 결과 출력:", Sum)

# [예제.5]
def dic_func(**par):
    print(par,type(par))
    for i in par.keys():
        print("{} : {}".format(i,par[i]))
dic_func(파이썬 = "3시간", C언어 = "3시간")

# [예제.6]
def change(a,b,c):
    return a+10,b+20,c+30

A = change(10,20,30)
print(A, type(A))

n1,n2,n3 = change(10,20,30)
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

# [문제.1]
def programinfo():
    print("Version : 1.x")
    print("Update Date : 2017-01-01")
    print("Author : Project Python")
programinfo()

# [문제.2]
def inc(number):
    print(number + 1)
def dec(number):
    print(number - 1)
inc(10)
dec(10)

# [문제.3]
def inc(num):
    return num + 1
def dec(num):
    return num - 1
# print(inc(10))
# print(dec(10))
a = inc(10)
b = dec(10)
print(a,b)

# [문제.4]
from random import random
def rangeRand(number):
    return int(random * (number + 1))
print(rangeRand(20))

# [문제.5]
from random import random
def rangeRand(start,end):
    if start > end:
        return -1
    return start + int(random() * (end - start + 1))
print(rangeRand(10,20))

# [문제.6]
def calc(num1,num2=1,op='+'):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
print(calc(2,1,'-'))
print(calc(2,1))
print(calc(3))
print(calc(3,op='-'))

# [문제.7]
def vSum(*number):
    tot = 0
    for x in number:
        tot += x
    return tot
print(vSum(1,2,3))
print(vSum(1,2,3,4,5,6))
print(vSum(1,2,3,4,5,6,7,8,9))

# [문제.8] : 알바비 계산 프로그램 (함수사용)
# - 조건 : 시급-[8500원], 기본 근무시간-[8시간], 기본 근무일수-[30일]

def alba(day=30, time=8, won=8500):
    ret = day * time * won
    return ret
def display():
    num = int(input("1.풀타임 근무\n2.근무일수 지정\n번호선택 >> "))
    if num == 1:
        ret = alba()
    elif num == 2:
        day = int(input("일한 일수입력: "))
        ret = alba(day)
    print("급여 :", ret,"원")
display()
'''




