'''
from random import random
# print(random())
print(int(random()*10))

lst = [1,2,3]
print("첫 번째 출력:",lst)
lst.append('a')
print("두 번째 출력:",lst)
lst.append([100,200])
print("세 번째 출력:",lst)
a=[100,200,300]
print(a,type(a))
lst.extend([400,500])
print("네 번째 출력:",lst)
# extend 함수는 리스트 안에 있는 요소들을 확장시키는 방식으로 늘어남
lst.insert(1,'insert')
print("다섯번째 출력:",lst)
# 1번 인덱스 부분에 insert라는 str형 문자열을 추가한다

numbers = [10,20,30,40,50,60,70]
Sum = 0
for i in numbers:
    print(i)
    Sum += i
print(Sum)

# 오늘의 로또번호
from random import random
numbers = []
cnt = 0 #특별한 숫자를 세주는 변수
while True:
    rand = int(random() * 45) + 1
    if rand not in numbers:
        numbers.append(rand)
        cnt += 1
        if cnt == 6:
            break
numbers.sort()

print(numbers)

gugu = []
for x in range(2,10):   # gugu [[1,2...9],[2,4...18], ~ ]
    gugu.append([])
    for y in range(1,10):
        gugu[x-2].append(x*y)
for x in range(2,10):
    for y in range(1,10):
        print("{}X{}={}".format(x,y,gugu[x-2][y-1]),end="\t")
    print()
'''
'''
import copy, os
info={}; data=[]; data2=[]
while True:
    print("=" * 20)
    print("1. 일정표 등록")
    print("2. 일정표 검색")
    print("3. 프로그램 종료")
    print("=" * 20)
    num = int(input("번호선택 >> "))
    if num == 1:
        data.append(input("날짜 입력: "))
        print("시간 별 일정을 등록해주세요.")
        time = int(input("몇 개의 일정을 등록하시겠습니까? "))
        for i in range(time):
            data2.append(input("형식->[시간:할일]: "))
        info[data[0]] = copy.copy(data2)
        data.clear()
        data2.clear()
    elif num == 2:
        day = input("일정을 확인 할 날짜 입력: ")
        if info.get(day) == None:
            print("해당 날짜에는 일정이 없습니다.")
        else:
            print("{}에 일정은 {} 입니다.".format(day,info.get(day)))
    elif num == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("번호를 다시 선택하세요.")
    os.system("pause")
    os.system("cls")
'''

'''
[ Quiz.2 ]: 학생의 인적 사항 등록 후 검색 하는 프로그램을 만드시오 
(학번, 이름, 주소, 등급(A,B,C,D,E,F)
dic -> { 1-123 : {학번 : 1-123, 이름 : 홍길동, 주소 : 경기도, 등급 : A}}
1.학생 등록
2.학생 검색
3.학생 수정
4.학생 삭제
5.전체 학생 목록
6.종료
'''
