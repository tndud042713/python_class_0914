'''
# [함수 활용 예제.1 ] : Reverse
def reversecode():
    result = int(input("수 입력:"))
    while True:
        tmp = result % 10
        result = result // 10
        print(tmp,end="")
        if not result:
            break
print("프로그램 시작")
reversecode()
print("\n프로그램 종료")

# [함수 활용 예제.2 ] : 자판기 메뉴선택
def sel_machine():
    sel = int(input("음료 선택\n1.콜라\n2.사이다\n3.환타\n번호선택 >> "))
    if sel == 1:
        print("콜라")
    elif sel == 2:
        print("사이다")
    elif sel == 3:
        print("환타")
    else:
        print("번호를 잘못 선택하셨습니다.")
sel_machine()

# [ 함수 활용 예제.3 ] : 함수 내부에서 또 다른 함수 호출
def showAvrg():
    a,b = int(input("첫 번째 정수입력: ")), int(input("두 번째 정수입력: "))
    ret = calc(a,b)
    print("{}과(와) {}의 평균".format(a,b))
    print("값은 {:.2f} 입니다.".format(ret))
def calc(a,b):
    ret = (a + b) / 2
    return ret
showAvrg()

# [ 함수 활용 예제.4 ] : 함수 내부에서 또 다른 함수 호출
def func2(a,b):
    a += 5; b += 10
    print("func2 a:{}, b:{}".format(a,b))
def func1():
    a = 5; b = 10
    func2(a,b)
    print("func1 a:{}, b:{}".format(a,b))
func1()

# [Quiz]
# 1. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해 주세요.
# 2. 예제 거꾸로 수를 반환하는 함수를 계산,출력 기능으로 나눠서 작성해 주세요.
# 3. 예제 자판기를 선택,출력 기능으로 나눠서 함수화 하여 작성해 주세요.

# [Quiz.1]
def calc(su1,op,su2):
    if op == '+':
        Output(su1,op,su2,su1+su2)
    elif op == '-':
        Output(su1,op,su2,su1-su2)
    elif op == '*':
        Output(su1,op,su2,su1*su2)
    elif op == '/':
        Output(su1,op,su2,su1/su2)

def Output(su1,op,su2,ret):
    print(su1,op,su2,"=",ret)

def InPut():
    su1,op,su2 = int(input("첫번째 정수입력: ")), input("부호입력: "), int(input("두번째 정수입력: "))
    calc(su1,op,su2)
InPut()

# [Quiz.2]
def ReverseCode(num):
    ret = 0
    while True:
        tmp = num % 10
        num = num // 10
        ret = (ret + tmp) * 10
        if not num:
            return ret // 10
def OutPut():
    num = int(input("거꾸로 반환할 정수 입력: "))
    ret = ReverseCode(num)
    print("변환 전 값:{}, 변환 후 값: {}".format(num,ret))
OutPut()

# [Quiz.3]
def sel_machine(sel):
    ret = ''
    if sel == 1:
        ret = "콜라"
    elif sel == 2:
        ret = "사이다"
    elif sel == 3:
        ret = "환타"
    else:
        return "번호를 잘 못 선택하셨습니다."
    if sel >= 1 and sel <= 3:
        return ret + "맛있게 드세요!"

def OutPut():
    sel = int(input("음료 선택\n1.콜라\n2.사이다\n3.환타\n번호선택 >> "))
    ret = sel_machine(sel)
    print(ret)
OutPut()
'''
# [ Lambda 함수 ]
'''
def swap(x,y):
    return y,x
a=10; b=20
print("변경 전:",a,b)
a, b = swap(a,b)
print("변경 후:",a,b)

swap = lambda a,b:[b,a]
a = swap(10,20)
print(a)

lam = lambda a:a*10
hap = lambda a,b:a+b
noData = lambda : print("No Data!")
print(lam(10))
print(hap(200,300))
noData()

# [Quiz] : 람다 함수를 이용하여 사칙연산 계산기를 프로그램을 제작하세요
Sum = lambda a,b:a+b
Sub = lambda a,b:a-b
Mul = lambda a,b:a*b
Div = lambda a,b:a/b

print(Sum(10,20))
print(Sub(10,20))
print(Mul(10,20))
print(Div(10,20))

# [모듈 및 패키지 만들기]
import calc
print(calc.sumFunc(100,200))
print(calc.subFunc(100,200))
print(calc.mulFunc(100,200))
print(calc.divFunc(100,200))

from calc import sumFunc, subFunc
print(sumFunc(100,200))
print(subFunc(100,200))
print(mulFunc(100,200))
print(divFunc(100,200))

from calc import *
print(sumFunc(100,200))
print(subFunc(100,200))
print(mulFunc(100,200))
print(divFunc(100,200))

from calc import *
print(sumFunc(100,200))
print(subFunc(100,200))
print(mulFunc(100,200))
print(divFunc(100,200))
'''
from pack import *
print(sum.sumFunc(10,20))
print(sub.subFunc(10,20))





