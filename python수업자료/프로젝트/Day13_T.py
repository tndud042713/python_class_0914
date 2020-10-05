'''
# [문제.1]
numbers = [10,20,30,40,50,60,70]
Sum = 0
for i in numbers:
    Sum += i
print(Sum)

# [문제.2]
from random import random
numbers = []
cnt = 0
while True:
    rand = int(random() * 45) + 1
    if rand not in numbers:
        numbers.append(rand)
        cnt += 1
        if cnt == 6:
            break
numbers.sort()
print(numbers)

# [문제.3]
lst_sec = [["홍길동","남",36],["김수양","여",32],["박담소","남",28]]
for val in lst_sec:
    print("이름: {}".format(val[0]))
    print("성별: {}".format(val[1]))
    print("나이: {}".format(val[2]))
    print(val,"\n")

# [문제.4] :[[1단],[2단],[3단],[4단],[5단],[6단],[7단],[8단],[9단]]
gugu = []
for x in range(2,10):   # gugu [[1,2...9],[2,4...18], ~ ]
    gugu.append([])
    for y in range(1,10):
        gugu[x-2].append(x*y)
for x in range(2,10):
    for y in range(1,10):
        print("{}X{}={}".format(x,y,gugu[x-2][y-1]),end="\t")
    print()

[ Tuple ]
- 사전적 의미는 List와 비슷 하다.
- List = "목록" , Tuple = "n개의 요소로 된 집합"
- List 와 Tuple의 차이점 
1. 정의 형식 List = [] , tuple = ()
2. List는 데이터 변경이 가능 , Tuple은 데이터 변경이 불 가능
3. List 데이터 목록 다루는데 적합하다.
4. Tuple은 위경도 , 좌표 , RGB색상표 등 변경이 없어야 하는 데이터를 처리 하는데 적합

※ 변경이 불가능한 자료형이 필요한 이유
[ 성능 ]
- 변경 가능한 자료형 과는 달리 데이터를 할당할 공간의 내용이나 크기가 달라지지 않기 때문에 생성 과정이 간단하다.
- 데이터가 오염되지 않을 것이라는 보장이 있기 때문에 복사본을 만드는 대신 그냥 원본을 사용

[ 신뢰 가능한 코드 ]
- 변경되지 않아야 할 데이터를 오염시키는 버그를 만들 가능성 제거
- 코드를 설계할 때부터 변경이 가능한 데이터와 그렇지 않은 데이터를 정리해서 코드에 반영

# [예제.1]
tu = (1,2,3,4,5)
print(tu,type(tu))
print(tu[0])
print(tu[1])
print(tu[-1])
print(tu[0:3])
print(tu[2:5])
# tu[0] = 100 : 튜플은 데이터 값을 변경 할 수 없다!!!!

# [예제.2]
tu = "문자열", 100, 123.456
print(tu,type(tu))
tu1 = (1)
print(tu1,type(tu1))
tu2 = (2,)
print(tu2,type(tu2))
tu3 = 3,
print(tu3,type(tu3))

# [예제.3]
a = (1,2,3)
b = (4,5,6)
c = a + b # 튜플 병합
print(a,type(a))
print(b,type(b))
print(c,type(c))

a += b # 기존 튜플 확장
print(a,type(a))

# [예제.4]
pack = (1,2,"packing")
print("Packing Tuple :", pack)
a,b,c = pack
print("Unpacking a:{}, b:{}, c:{}".format(a,b,c))

# [예제.5]
tu = (100,200,"함수",100,"테스트")
print("100 데이터의 갯수:",tu.count(100))
print("200 데이터의 인덱스번호:",tu.index(200))

# [예제.6]
tu = (1,2,3,4,5)
lst = list(tu)
print(lst,type(lst))

for val in tu:
    print(val)
'''
# [문제.1]
numbers = (10,20,30,40,50,60,70)
num1 = numbers[numbers.index(30)]
num2 = numbers[numbers.index(40)]
print("num1 Data:",num1)
print("num2 Data:",num2)

# [문제.2]
menu = (("칼국수", 6000),("비빔밥",5500),("돼지국밥",7000))
for val in menu:
    print("{} - {:,}원".format(val[0],val[1]))



