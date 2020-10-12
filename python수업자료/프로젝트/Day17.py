'''
# 1번 문제
profile = input("이름과 나이를 입력하시오, 단 공백으로 구분됩니다: ")
print(profile.split(" "))

#강사풀이
# 첫번째 풀이
user = input("이름과 나이를 입력하세요: ")
lst = user.split()
print("이름 : {}, 나이:{}".format(lst[0],lst[1]))
# 두번째 풀이
name,age = user.split()
print("이름 : {}, 나이:{}".format(name,age))



# 2번 문제


#강사풀이
ex = input("수식입력(EX:5 * 5): ")
if '+' in ex:
    num1, num2 = ex.split('+')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print("{} = {}".format(ex,num1+num2))
elif '-' in ex:
    num1, num2 = ex.split('-')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print("{} = {}".format(ex,num1-num2))
elif '*' in ex:
    num1, num2 = ex.split('*')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print("{} = {}".format(ex,num1*num2))
elif '/' in ex:
    num1, num2 = ex.split('/')
    num1 = int(num1.strip())
    num2 = int(num2.strip())
    print("{} = {}".format(ex,num1/num2))
else:
    print("잘못입력")

# 예제.4
def func1():
    print("func1 함수 실행!")
print("함수 실행 전!")
func1()
print("다음 문장 실행!")

# 예제.5
def func2(arg1,arg2):
    print(arg1, arg2)
func2(100,200)
func2('A','B')
func2(10.123,20.456)

#예제.6
def func3(arg=1): #인자값을 설정하지 않았을 때는 default 매개변수로 설정됨
    print(arg) #인자값을 설정할때는 아래의 식을 따른다.
func3(100)
func3()

#예제.7
def func4(arg1=1, arg2=1):
    print(arg1,arg2)
func4(100)
func4(100,200)
func4(arg2=100) #두번째 매개변수도 default 매개변수를 지정할 수 있다
'''
'''
[스코핑 룰]
1. 지역변수는 한정된 지역(local)에서만 사용되는 변수,
   함수 내부에서 사용되는 지역 변수는 함수 내에서 선언.

2. 전역변수는 프로그램 전체(Global)에서 사용되는 변수,
   모든 코드에서 사용하는 전역 변수는 함수 바깥쪽에 선언.

함수 내부에서 선언되는 변수는 거의 지역변수라고 하고
함수 외부에서 선언되는 변수는 거의 전역변수라고 한다
우리가 지금까지 사용한 변수는 전역변수에 가깝다.

전역변수의 단점 : 전체 프로그램이 다 동작하고 끝나야지만 전역변수 선언했던
메모리 공간을 반환한다 - 메모리 사용률이 비효율적이다.
반면에 지역변수는 특정함수 내에서 호출되고 특정함수가 사용되면 반환된다.
따라서, 지역변수는 메모리 사용률이 효율적이다.

왠만하면 지역변수를 사용하도록 유도하는 것이 효과적이다.
'''
'''
#예제.8
def func1():
    a=100
    print("func1의 a 변수: ",a)
def func2():
    a=200
    print("func2의 a 변수: ",a)
func1()
func2()
# 예제.9
def func1():  
    print("func1의 a 변수: ",a)
def func2():
    print("func2의 a 변수: ",a)
a=1000
func1()
func2()

#예제.10
a=100
def func1():
    a=10
    print(a)
func1()
# 지역변수와 전역변수가 이름이 같을 경우 지역변수의 우선순위가 더 높다

# 예제.11
# 함수 내에서 전역변수를 바꾸고 싶은 경우 -global 이라는 지시자를 이용-
a=100
def func1():
    global a #전역변수로 인식하게 된다
    a=10
    # global a=10 #이런식으로 쓰면 에러가 난다. 위와같이 써야한다
    print(a)
func1() #지역변수의 값 출력
print(a) #전역변수의 값 출력

# 퀴즈1
num =10
sum = 0
def display():
    sumFunc()
    print("10까지의 합 : ",sum)
def sumFunc():
    global sum
    for i in range(num+1):
        sum+=i
display()
'''
