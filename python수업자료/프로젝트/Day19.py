'''
# 함수 활용 예제.1
# 코드 동작원리 한번 생각 해 볼 것
def reversecode():
    result = int(input("수 입력: "))
    while True:
        tmp = result % 10
        result = result//10 #정수연산 하겠다는 뜻
        print(tmp,end="")
        if not result: # result가 거짓이 되어야 앞에 not때문에 참이 됨
            break;

print("프로그램 시작")
reversecode()
print("프로그램 종료")

# 함수 활용 예제.2

def sel_machine():
    sel = int(input("음료선택\n1.콜라\n2.사이타\n3.환타\n번호선택>>"))
    if sel == 1:
        print("콜라")
    elif sel == 2:
        print("사이다")
    elif sel == 3:
        print("환타")
    else:
        print("번호를 잘못 선택하셨습니다.")
sel_machine()

#함수 활용 예제.3 : 함수 내부에서 또 다른 함수 호출
#pass를 사용하여 함수의 이름만 미리 지정 할 수 있다.
def showAvrg():
    a,b = int(input("첫 번째 정수입력: ")), int(input("두 번째 정수입력: "))
    ret = calc(a,b)
    print("{}(와) {}의 평균".format(a,b))
    print("값은 {:.2f} 입니다.".format(ret))
def calc(a,b):
    ret = (a+b)/2
    return ret
showAvrg()

#함수 활용 예제.4 : 함수 내부에서 또 다른 함수 호출
def func2(a,b):
    a += 5; b += 10
    print("func2 a:{}, b:{}".format(a,b))
def func1():
    a = 5; b = 10
    func2(a,b)
    print("func1 a:{}, b:{}".format(a,b))
func1()
'''

'''
퀴즈
1. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해 주세요.
2. 예제 거꾸로 수를 반환하는 함수를 계산,출력 기능으로 나눠서 작성해 주세요.
3. 예제 자판기를 선택,출력 기능으로 나눠서 함수화 하여 작성해 주세요
'''
'''
# 퀴즈1
def inputing():
    print("두수와 연산을 입력하시오")
    a = int(input("첫번째 입력할 수 : "))
    op = input("시행하고자 하는 연산(사칙 연산 중 하나): ")
    b = int(input("두번째 입력할 수 : "))
    calc(a,op,b)

def calc(a,op,b):
    if(op=='+'):
        cal=a+b
        printing(cal)
    elif(op=='-'):
        cal=a-b
        printing(cal)
    elif(op=='*'):
        cal=a*b
        printing(cal)
    elif(op=='/'):
        cal=a/b
        printing(cal)
    else:
        print("잘못된 입력입니다.")
    
def printing(cal):
    print("입력하신 수의 연산은 {}입니다 ".format(cal))

inputing()




# 퀴즈2 - 잘 풀긴 했으나 강사풀이가 신박하므로 꼭 비교해보기
lst=[]
def reversecode():
    result = int(input("수 입력: "))
    
    while True:
        tmp = result % 10
        result = result//10 #정수연산 하겠다는 뜻
        lst.append(tmp)
        if not result: # result가 거짓이 되어야 앞에 not때문에 참이 됨
            break
    printing()

def printing():
    for i in lst:
        print(i,end="")
    print()

print("프로그램 시작")
reversecode()
print("프로그램 종료")


# 퀴즈3
def sel_machine():
    sel = int(input("음료선택\n1.콜라\n2.사이타\n3.환타\n번호선택>>"))
    if sel == 1:
        a="콜라"
    elif sel == 2:
        a="사이다"
    elif sel == 3:
        a="환타"
    else:
        a=False
    printing(a)
    
def printing(a):
    if a==False:
        print("잘못 주문하셨습니다.")
    else:
        print("주문하신 음료는 {}입니다.".format(a))
sel_machine()

#강사풀이는 수업 다 끝나고 프로젝트 파일 참고해서 복습할 것
'''
'''
# [lambda 함수]
def swap(x,y):
    return y,x #리턴 순서를 변경하는 방식으로 swap한다

a=10; b=20
print("변경 전:",a,b)
a,b = swap(a,b) #unpacking하므로써 a,b 값이 교환된다.
print("변경 후:",a,b)

swap = lambda a,b:(b,a) #()튜플로 묶는것도 되고 []리스트로 묶는것도 가능하다
a= swap(10,20)
print(a)

lam = lambda a: a*10
hap = lambda a,b: a+b
noData = lambda : print("No Data!")
print(lam(10))
print(hap(200,300))
noData() #인자 값 없는 람다식의 활용


#퀴즈:lambda함수를 이용하여 사칙연산 계산기 프로그램을 작성하시오
plus = lambda a,b: a+b
minus = lambda a,b: a-b
multiple = lambda a,b: a*b
division = lambda a,b: a/b

print(plus(150,10))
print(minus(150,10))
print(multiple(150,10))
print(division(150,10))
'''
'''
# 모듈 및 패키지 만들기
# 같은 작업공간에 존재해야 모듈을 사용 할 수 있다.
import calc
print(calc.sumFunc(100,200))
print(calc.subFunc(100,200))
print(calc.mulFunc(100,200))
print(calc.divFunc(100,200))


from calc import sumFunc, subFunc
#from 정의자를 사용하면 calc는 정의되있으므로 calc. 이런식으로 적어줄 필요가 없음
print(sumFunc(100,200))
print(subFunc(100,200))
# print(mulFunc(100,200)) #정의가 안됬으므로
# print(divFunc(100,200)) #에러메세지를 띄운다

from calc import * # 다불러올 때는 *을 사용한다
#from 정의자를 사용하면 calc는 정의되있으므로 calc. 이런식으로 적어줄 필요가 없음
print(sumFunc(100,200))
print(subFunc(100,200))
print(mulFunc(100,200))
print(divFunc(100,200))

'''
from pack import *
print(sum.sumFunc(10,20))
print(sub.subFunc(10,20))
#빨간색 밑줄은 그어지지만 정상적으로 실행이 된다.

#패키지를 만들일은 흔하지 않고 모듈을 만들일은 흔하다!!