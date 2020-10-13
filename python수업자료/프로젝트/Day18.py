'''
# 예제.1
def func1(a):
    if a==1:
        return
        print("함수실행") # return 아래는 실행이 안됨
func1(1)
print("프로그램 실행종료")

# 예제.2
def func2():
    print("함수실행")
    a = input("리턴값 입력: ")
    return a
ret = func2()
print("리턴값 출력:",ret)

# 예제.3
def calc(su1,su2):
    ret = su1 + su2
    print("계산기실행")
    return ret
su1, su2 = int(input("정수입력: ")), int(input("정수입력: "))
result = calc(su1,su2)
print(su1,"+",su2,"=",result)

# 예제.4
def sum_func(*par):
    print(par,type(par))
    result =0
    for i in par:
        result += i
    return result

Sum = sum_func(10,20)
print("첫 번째 결과 출력: ",Sum)
Sum = sum_func(10,20,30,40,50)
print("두 번째 결과 출력: ",Sum)


#예제.5
def dic_func(**par):
    print(par,type(par))
    for i in par.keys():
        print("{} : {}".format(i,par[i]))


dic_func(파이썬 = "3시간", C언어 = "3시간")

#예제.6
def change(a,b,c):
    return a+10,b+20,c+30

A = change(10,20,30)
print(A,type(A))

n1,n2,n3 = change(10,20,30)
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

# PDF문제
# 문제.1
def programInfo():
    print("Version :","1.x")
    print("Update Date :","2017-01-01")
    print("Author :","Project python")
programInfo()

#문제.2
def inc(number):
    print(number+1)
def dec(number):
    print(number-1)
number=int(input("수를 입력하시오: "))
inc(number)
dec(number)

#문제.3
def inc(number):
    return number+1
def dec(number):
    return number-1
number=int(input("수를 입력하시오: "))
print(inc(number))
print(dec(number))

#문제.4
def rangeRand(number):
    from random import random
    rand=int(random()*number)+1
    return rand
    
number=int(input("랜덤으로 뽑고싶은 수를 입력하시오: "))
print(rangeRand(number))
#강사풀이
from random import random
def rangeRand(number):
    return int(random()*number )+ 1
print(rangeRand(20))



#문제.5
def rangeRand(start,end):
    from random import random
    rand=int(random()*(end-start))+start+1
    return rand

start=int(input("랜덤으로 첫번째 범위를 입력하시오: "))
end=int(input("랜덤으로 마지막 범위를 입력하시오: "))
print(rangeRand(start,end))


# 문제.6
def calc(num1,num2=1,op='+'):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2    

print(calc(2,1,'-'))
print(calc(2,1))
print(calc(3))
print(calc(3,op='-'))


#문제.7
def vSum(*ptr):
    sum=0
    for i in ptr:
        sum+=i
    return sum

print(vSum(1,2,3))
print(vSum(1,2,3,4,5,6))
print(vSum(1,2,3,4,5,6,7,8,9))

'''
# 문제.8 : 알바비 계산 프로그램(함수사용)
# - 조건 : 시급-[8500원], 기본 근무시간-[8시간], 기본 근무일수-[30일]

def paycalc(day=30,time=8):
    pay=int(8500*time*day)
    return pay
print("이번달 알바비는 {:,}원 입니다.".format(paycalc(24,12)))
print("이번달 알바비는 {:,}원 입니다.".format(paycalc())) #기본값 출력

# 강사풀이
def alba(day=30, time=8, won=8500):
    ret = day*time*won
    return ret

def display():
    num=int(input("1.풀타임 근무\n2.일한 날짜 입력\n번호선택>>"))
    if num==1:
        ret=alba()
    elif num==2:
        day = int(input("일한 일수입력: "))
        ret = alba(day)
    print("급여 : {:,}원 입니다.".format(ret))

display()