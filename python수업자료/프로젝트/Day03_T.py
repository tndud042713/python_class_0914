'''
#[예제.1]
var1 = 1
var2 , var3 = 2 , 3
var4 = var5 = 4
print("var1 = {}".format(var1))
print("var2 = {}".format(var2))
print("var3 = {}".format(var3))
print("var4 = {}".format(var4))
print("var5 = {}".format(var5))

#[예제.2]
v1 = "1"
v2 = 1
v3 = 1.0
print("v1 Data: {}\tv1 Type: {}".format(v1,type(v1)))
print("v2 Data: {}\tv2 Type: {}".format(v2,type(v2)))
print("v3 Data: {}\tv3 Type: {}".format(v3,type(v3)))

#[예제.3]
v1 , v2 , v3 = "1" , 1 , 1.0
print(type(v1))
print(type(v2))
print(type(v3))
print("\n\n")

v1 = int(v1)
v2 = float(v2)
v3 = str(v3)
print(type(v1))
print(type(v2))
print(type(v3))

#[예제.4]
num1 = 100
num2 = 200
TEST = num1 + num2
print("TEST 변수의 값: {}".format(TEST))

# [문제.1] : num1(10) + num2(20) = 30 출력해 주세요.
# 단, 10 , 20 , 30 은 변수를 이용하여 출력

# [문제.2] 
# num1 = 7 
# num2 = 5
# 위 값의 연산 결과를 각각의 변수에 저장 후 출력 (+,-,*,/) 

# [문제.3]
#1. 다음과 같이 나오도록 코딩 하세요. ( 단, 변수를 사용 할 것 ) Python 100점 !!!
#2. 다음과 같이 나오도록 코딩 하세요. ( 단, 변수를 사용 할 것 ) 나는 20살입니다. ^^!
#3. Python , C언어 , Java 3과목의 점수를 각 변수에 저장
# 합계와 평균을 구하는 프로그램을 만드시오. ( 평균은 소수점 2자리 까지 )

# [문제.1]
num1 = 10
num2 = 20
print("num1({}) + num2({}) = {}".format(num1,num2,num1+num2))

# [문제.2]
num1 = 7
num2 = 5
print("{} + {} = {}".format(num1,num2,num1+num2))
print("{} - {} = {}".format(num1,num2,num1-num2))
print("{} * {} = {}".format(num1,num2,num1*num2))
print("{} / {} = {}".format(num1,num2,num1/num2))

#[문제.3]
str1 = "Python 100점!!!"
str2 = "나는 20살 입니다. ^^!"
print(str1)
print(str2)

py = 100
java = 77
c = 66
Sum = py + java + c
avg = Sum / 3
print("3과목의 총점:", Sum)
print("3과목의 평균: {:.2f}".format(avg))

# [문제.4]
# su = 100
# num ='100'
# fit = 1.111
# 변수들을 선언 후 위 변수를 이용하여 아래와 같은 출력 결과가 나오도록 코드를 완성하세요.

# [ 출력 결과 ]
# 200
# 101.111
# 100100

# [문제.4]
su = 100
num ='100'
fit = 1.111
print(su + int(num))
print(float(su) + fit)
print(str(su) + num)
# 문자열 + 문자열 가능하다 ( 문자열 이어붙이기 )

# [input] 
# - 데이터를 입력받는 함수 (print함수의 반대 개념)
# - 데이터를 입력 받을 경우 기본값 ★"문자열"★로 인식
# - 값을 입력받아 연산을 진행 할 경우 형변환 하여 입력을 받아야 한다

#[예제.5]
num1 = input("첫 번째 정수입력: ")
num2 = input("두 번째 정수입력: ")
print("num1 Data: {}\tnum2 Data: {}".format(num1, num2))
print("num1 Type: {}\tnum2 Type: {}".format(type(num1), type(num2)))
print(int(num1) + int(num2))

#[예제.6]
num1 = int(input("첫 번째 정수입력: "))
num2 = int(input("두 번째 정수입력: "))
print("num1 Data: {}\tnum2 Data: {}".format(num1, num2))
print("num1 Type: {}\tnum2 Type: {}".format(type(num1), type(num2)))
print(num1 + num2)

[ 입력 함수 Quiz ]
학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오
학생 이름 : 강사
국어 점수 : 1
영어 점수 : 2
수학 점수 : 2
=================학생 정보==================
이름  국어  영어  수학  합계  평균
강사   1     2     2    5    1.67

name = input("학생 이름: ")
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
mat = int(input("수학 점수: "))
print("===================== 학생정보 =====================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3))
'''

#[문제.1]
name = input("이름입력:")
age = int(input("나이입력:"))
print("{}님의 나이는{}입니다.".format(name,age))

#[문제.2]
num1 = int(input("첫 번째 정수 입력:"))
num2 = int(input("두 번째 정수 입력:"))
result = num1 + num2 
print("num1 + num2 = {}".format(result))
result = num1 - num2 
print("num1 - num2 = {}".format(result))
result = num1 * num2 
print("num1 * num2 = {}".format(result))
result = num1 / num2 
print("num1 / num2 = {}".format(result))

#[문제.3]
name=input("이름:")
tall=float(input("키:"))
weight=float(input("체중:"))
std_weight = (tall-100) * 0.9
pat = weight / std_weight * 100
print("{}님의 비만도는 {:.2f}% 입니다.".format(name,pat))






