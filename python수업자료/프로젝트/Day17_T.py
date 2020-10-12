'''
# [예제.1]
st = "Never Ever Give Up"
print(st)
print(st.split())
lst = st.split()
print(lst,type(lst))

# [예제.2]
st = "하나:둘:셋"
print(st.split(":"))
print(st.split())
print(st.splitlines())

st = """하나:둘:셋
하나:둘:셋
하나:둘:셋"""
print(st.splitlines())

# [예제.3]
st = "123"
print('%'.join(st))
lst = ["안녕하세요", "반갑습니다", "또만나요"]
print("\n".join(lst))
print(" ".join(lst))

# [문제.1]
user = input("이름과 나이를 입력하세요: ")
# lst = user.split()
# print("이름:{}, 나이:{}".format(lst[0],lst[1]))

name, age = user.split()
print("이름:{}, 나이:{}".format(name,age))

# [문제.2]
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
    print("잘못 입력")

# [예제.4]
def func1():
    print("func1 함수 실행!")
print("함수 실행 전!")
func1()
print("다음 문장 실행!")

# [예제.5]
def func2(arg1,arg2):
    print(arg1,arg2)
func2(100, 200)
func2('A', 'B')
func2(10.123, 20.456)

# [예제.6]
def func3(arg=1):
    print(arg)
func3(100)
func3()

# [예제.7]
def func4(arg1=1,arg2=1):
    print(arg1,arg2)
func4(100)
func4(100,200)
func4(arg2=100)

[스코핑 룰]
1. 지역변수는 한정된 지역(Local)에서만 사용되는 변수, 
   함수 내부에서 사용되는 지역 변수는 함수 내에서 선언.
2. 전역변수는 프로그램 전체(Global)에서 사용되는 변수, 
   모든 코드에서 사용하는 전역 변수는 함수 바깥쪽에 선언.


# [예제.8]
def func1():
    a = 100
    print("func1의 a 변수:", a)
def func2():
    a = 200
    print("func2의 a 변수:", a)
func1()
func2()

# [예제.9]
def func1():
    print("func1의 a 변수:", a)
def func2():
    print("func2의 a 변수:", a)  
a = 1000
func1()
func2()

# [예제.10]
a = 100
def func1():
    a = 10
    print(a)
func1()

# [예제.11]
a = 100
def func1():
    global a
    a = 10
    print(a)
func1()
print(a)

# [Quiz.1] : 위 코드를 전역변수를 사용하는 코드로 변경하세요.
def display():
    num = 10
    print("10까지의 합 : " , sumFunc(num))
def sumFunc(num) :
    sum=0
    for i in range(num+1):
        sum+=i
    return sum
display()

num = 10
sum = 0
def display():
    sumFunc()
    print("10까지의 합 : " , sum)
def sumFunc():
    global sum
    for i in range(num+1):
        sum+=i
display()
'''


