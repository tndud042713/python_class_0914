# 예제.1

# var1 = 1
# var2,var3 = 2,3
# var4=var5=4

# print("var1 = {}".format(var1))
# print("var2 = {}".format(var2))
# print("var3 = {}".format(var3))
# print("var4 = {}".format(var4))
# print("var5 = {}".format(var5))

# 예제.2
# v1 = "1" #쌍따옴표를 보고 컴파일러는 문자열로 인식하게 된다.
# v2 = 1 #컴파일르는 그냥 정수로 인식한다.
# v3 = 1.0 #컴파일러가 실수로 인식한다.

# print("v1 Data: {}, v1 Type: {}".format(v1,type(v1)))
# print("v2 Data: {}, v2 Type: {}".format(v2,type(v2)))
# print("v3 Data: {}, v3 Type: {}".format(v3,type(v3)))

#예제.4
# num1 = 100
# num2 = 200
# TEST = num1+num2
# print("TEST 변수의 값: {}".format(TEST))

# # 문제 스스로 풀기
# print("문제1")
# num1=10
# num2=20
# num3=num1+num2
# print("num1({}) + num2({}) = {}".format(num1,num2,num3))
# print("\n")

# print("문제2")
# num_1 = 7
# num_2 = 5

# print("두수의 합은 {}이다.".format(num_1+num_2))
# print("두수의 차는 {}이다.".format(num_1-num_2))
# print("두수의 곱은 {}이다.".format(num_1*num_2))
# print("두수의 제는 {}이다.".format(num_1/num_2))
# print("\n")

# print("문제3")
# print("1:")
# str="Python 100점!!!"
# print(str)
# print("2:")
# age=26
# print(f"나는 {age}살입니다. ^^!")
# print("3:")

# python = int(input("파이썬 점수를 입력하세요: "))
# C = int(input("C언어 점수를 입력하세요: "))
# Java = int(input("Java 점수를 입력하세요: "))
# avg=float((python+C+Java)/3)
# print("3과목의 평균은 {:.2f}점 입니다".format(avg))

# 문제4
# su=100
# num ='100'
# fit = 1.111

# print(su+int(num))
# print(su+fit)
# print(int(su)+fit)
# print(str(su)+num)

# name=input("학생이름 : ")
# kor=int(input("국어점수 : "))
# eng=int(input("영어점수 : "))
# mat=int(input("수학점수 : "))
# sum=kor+eng+mat
# avg=float(sum/3)
# print("=====================================")
# print("이름\t국어\t영어\t수학\t합계\t평균\t")
# print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,mat,sum,avg))

# pdf 문제

# name = input("이름을 입력하시오 : ")
# age = input("나이를 입력하시오 : ")

# print(f"{name}님의 나이는{int(age)}세 입니다.")

# num1= int(input("첫번째 숫자를 입력하시오"))
# num2= int(input("두번째 숫자를 입력하시오"))

# print("각 숫자들의 사칙연산 결과는")
# print("{} + {} = {}".format(num1,num2,num1+num2))
# print("{} - {} = {}".format(num1,num2,num1-num2))
# print("{} * {} = {}".format(num1,num2,num1*num2))
# print("{} / {} = {}".format(num1,num2,num1/num2))

name = input("이름을 입력하시오 : ")
h=float(input("키를 입력하시오 : "))
w=float(input("체중을 입력하시오 : "))
std=(h-100)*0.9
bmi=(w/std)*100
print("{}님의 비만도는 {:.2f}%입니다.".format(name,bmi))

