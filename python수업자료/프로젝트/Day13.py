# pdf26페이지 문제풀이
#======================================================================

# 1번 내풀이 //스스로 풀었음
# numbers = [10, 20, 30, 40, 50, 60, 70]
# sum=0
# for i in range(len(numbers)-1,0,-1):
#     sum+=numbers.pop(i)
# print(sum)

# 강사풀이
# numbers = [10, 20, 30, 40, 50, 60, 70]
# sum=0
# for i in numbers:
#     sum+=i
# print(sum)
#======================================================================

# 2번 내풀이 //중복없이에 대해서 해결하지 못했음
# from random import randint,randrange,random

# for i in range(6):
#     print(randrange(1,45,1))

#강사풀이
#로또 번호 출력 프로그램
# from random import random
# numbers = []
# cnt = 0
# while True:
#     rand = int(random() * 45)+1
#     if rand not in numbers:
#         numbers.append(rand)
#         cnt +=1
#         if cnt == 6:
#             break
# numbers.sort()
# print(numbers)
#================================================================
# 3번 내풀이 //스스로 풀었음
# lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32],
# ['박담소', '남', 28]]

# for i in range(0,3,1):
#     name=lst_sec[i][0]
#     sex=lst_sec[i][1]
#     age=lst_sec[i][2]
#     print(name)
#     print(sex)
#     print(age)

# 강사 풀이
lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32],['박담소', '남', 28]]
for val in lst_sec:
    print("이름: {}".format(val[0]))
    print("성별: {}".format(val[1]))
    print("나이: {}".format(val[2]))
    print(val,"\n")

# 4번 내풀이 //시간내에 풀지 못했음
# [[1단],[2단],[3단],[4단],[5단],[6단],[7단],[8단],[9단]]

# 강사풀이
# gugu=[]
# for x in range(1,10): # gugu [[]]
#     gugu.append([])
#     for y in range(1,10):
#         gugu[x-1].append(x*y)

# for x in range(1,10):
#     for y in range(1,10):
#         print("{:2} x{:2} ={:3}".format(x,y,gugu[x-1][y-1]),end=" ")
#     print()
# print(gugu)
# for val in gugu:
#     print(val)

'''
[Tuple]
- 사전적 의미는 List와 비슷하다.
- List = "목록" , Tuple = "n개의 요소로 된 집합"
- List 와 Tuple의 차이점
1. 정의 형식 List = [] , tuple = ()
2. List 는 데이터 변경이 가능, Tuple은 제이터 변경이 불가능
3. List 데이터 목록 다루는데 적합하다.
4. Tuple은 위경도 , 좌표 , RGB색상표 등 변경이 없어야 하는 데이터를 처리 하는데 적합

** 변경이 불가능한 자료형이 필요한 이유
[성능]
- 변경 가능한 자료형과 달리 데이터를 할당할 공간의 내용이나 크기가 달라지지 않기 때문에 생성과정이 간단하다
- 데이터가 오염되지 않을 것이라는 보장이 있기 때문에 복사본을 만드는 대신 그냥 원본을 사용

[신뢰 가능한 코드]
- 변경되지 않아야 할 데이터를 오염시키는 버그를 만들 가능성 제거
- 코드를 설계할 때부터 변경이 가능한 데이터와 그렇지 않은 데이터를 정리해서 코드에 반영
'''

# # 예제.1
# tu = (1,2,3,4,5)
# print(tu,type(tu))
# print(tu[0])
# print(tu[1])
# print(tu[2])
# print(tu[3])
# print(tu[4])
# print(tu[0:3])
# print(tu[2:5])
# # tu[0] = 100
# # 튜플은 값의 변경이 불가능하다
# lst = [1,2,3]
# lst[0] = 100
# print(lst)
# # 리스트는 값의 변경이 가능하다

# # 예제.2
# tu = "문자열",100,123.456
# print(tu,type(tu))

# tu1 = (1)
# print(tu1,type(tu1))
# tu2 = (2,)
# print(tu2,type(tu2))
# tu3 = 3,
# print(tu3,type(tu3))
# # 쉼표의 유뮤가 튜플인지 아닌지 분별하는 요소이다

# # 예제.3
# # 튜플확장 및 튜플 정의
# a = (1,2,3)
# b = (4,5,6)
# c = a+b #튜플 병합
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))

# a+=b # 기존 튜플 확장
# print(a,type(a))

# # 예제.4
# pack = (1,2,"packing") 
# print("packing Tuple :",pack)

# a,b,c = pack #unpacking 작업
# print("Unpacking a:{} b:{} c:{}".format(a,b,c))

# 예제.5
# tu = (100,200,"함수",100,"테스트")
# print("100 데이터의 갯수:",tu.count(100)) #value가 몇개인지 세주는 함수
# print("200 데이터의 인덱스 번호:",tu.index(200)) #해당하는 value가 몇번 인덱스인지 알려주는 함수

# 예제.6
# tu = (1,2,3,4,5)
# lst = list(tu) #튜플을 리스트로 형변환
# print(lst,type(lst))

# for val in tu:
#     print(val)

# pdf 35 페이지 문제
# 1번문제 내풀이
# numbers = (10, 20, 30, 40, 50, 60, 70)
# num1=numbers[2]
# num2=numbers[3]
# print(num1,num2)

# 강사풀이
# numbers = (10, 20, 30, 40, 50, 60, 70)
# num1= numbers[numbers.index(30)]
# num2= numbers[numbers.index(40)]
# print("num1 Data:",num1)
# print("num2 Data:",num2)

#==========================================================

# 2번문제 내풀이
# menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥',7000))
# for val in menu:
#     print("{} - {}원".format(val[0],val[1]))

# #강사풀이
# menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥',7000))
# for val in menu:
#     print("{} - {:,}원".format(val[0],val[1])) #{:,}는 천단위 지정할때 쓰인다
