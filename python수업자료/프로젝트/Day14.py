'''

# 문제.1

# 내풀이

tu=("회사정보","제품명","가격정보","출시일")
for i in range(len(tu)):
    print(tu[i])

# 강사풀이
tu=(10,20,"Tuple","Test",111.222)
# for i in range(len(tu)):
#     print("Data:",tu[i])
for i in tu:
    print("Data:",i)


==========================================================


# 문제.2

# 내풀이

tu=("회사정보","제품명","가격정보","출시일")
li=["삼성전자","Galaxy","100원","미정"]


print("----------------------------------------------")
print("\t{:8}\t\t{:8}".format("(tuple)","(list)"))
for val in range(len(tu)):
    print("\t{:8}\t:\t{:8}".format(tu[val],li[val]))
print("----------------------------------------------")

# 강사풀이
# 내풀이와 거의 같아서 바꿀게 없다.




# 문제.3

# 내풀이

tu=("회사정보","제품명","가격정보","출시일")
li=["삼성전자","Galaxy","100원","미정"]


print("----------------------------------------------")
print("\t{:8}\t\t{:8}".format("(tuple)","(list)"))
for val in range(len(tu)):
    print("\t{:8}\t:\t{:8}".format(tu[val],li[val]))
print("----------------------------------------------")

print(li.index("100원"))
print(li.index("미정"))
li.remove("100원")
li.remove("미정")
li.insert(2,"110원")
li.insert(3,"이번 달 말")
for val in range(len(tu)):
    print("\t{:8}\t:\t{:8}".format(tu[val],li[val]))

#강사풀이
tu=("회사정보","제품명","가격정보","출시일")
li=["삼성전자","Galaxy","100원","미정"]
a= li.index("100원")
b= li.index("미정")
li.remove("100원")
li.remove("미정")
li.insert(a,"110원")
li.insert(b,"이번 달 말")

print("----------------------------------------------")
print("\t{:8}\t\t{:8}".format("(tuple)","(list)"))
for val in range(len(tu)):
    print("\t{:8}\t:\t{:8}".format(tu[val],li[val]))
print("----------------------------------------------")
'''
'''
[Dictionary] #--> {KEY1:[Value1,Value2,Value3],KEY2:[Value1,Value2,Value3]}
: List와 비슷하다, List와 같이 첨자를 이용하여 요소에 접근 한다.
: Dictionaty의 첨자는 Key를 사용한다.
: key가 가리키는 곳에 데이터를 저장.
: 탐색 속도가 빠르고, 사용하기 편리하다.
: Dictionary 정의 시 " { } "를 이용한다.
: 특정 슬롯에 새로운 key-Value를 입력하거나 Dictionary 안에 있는 요소를 참조 할 때에는 "[KEY]"를 사용.
'''
'''
# 예제.1
student = {"학번":"00-1234", "이름":"홍길동", "학과":"컴퓨터공학"}
print(student,type(student))
print(student["학번"])
print(student["이름"])
print(student["학과"])
'''
'''
#예제2
www={}
www["파이썬"]="www.python.org"
www["네이버"]="www.naver.com"
www["구글"]="www.google.com"
print(www,type(www))
print(www["파이썬"],type(www["파이썬"]))
print(www["네이버"],type(www["네이버"]))
print(www["구글"],type(www["구글"]))
'''
'''
# 예제.3
info ={}
key = input("키 값 입력: ")
val = int(input("정수 값 데이터 입력: "))
info[key] = val
print(info)
'''
'''
# 예제.4
info ={}
lst=[1,2,3,4,5]
tu=(6,7,8,9,10)
info["테스트"]=lst
info["파이썬"]=tu
print(info["테스트"])
print(info["파이썬"])
'''
'''
# Dictionary 문제
overwatch={}
for i in range(5):
    key = input("캐릭터명: ")
    value = input("궁극기: ")
    overwatch[key]=value
print(overwatch)
'''

'''
# 예제.5

# 대입연산자를 사용해서 업데이트가 가능하지만
# 업데이트 함수를 이용한 업데이트가 유용하기 때문에 익혀보자

dic={1:'a',2:'b',3:'c'}
print(dic)
dic.update({4:'d'})
# dic.update(4:'d') 이렇게 쓰면 구문오류가 발생한다
print(dic)
'''
'''
# 예제.6
dic={1:'a',2:'b',3:'c'}
print(dic)
print(dic.get(1)) #dic[1]
print(dic.get(2))
print(dic.get(3))
print(dic.get(4))
if dic.get(4) == None:
    print("해당 키값은 존재하지 않습니다.")
'''
'''
# 예제.7
key_list = [1,2,3,4,5]
dic1={}.fromkeys(key_list)
dic2={}.fromkeys(key_list,'a')
print(dic1)
print(dic2)
'''
'''
# 예제.8
dic={1:'a',2:'b',3:'c'}
print(dic.keys())
print(dic.values())
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic)) #기본값으로 키값을 반환한다.
'''
'''
# 예제.9
sub={}
sub["과목명"] = input("과목이름 입력:")
sub["수업시간"] = int(input("수업시간 입력: "))
print()
for i in sub.keys(): # for i in sub 만 써도 똑같이 출력된다
    print("{} : {}".format(i,sub[i]))
'''
'''
#예제.10
dic={1:'a',2:'b',3:'c'}
print(dic)
print(dic.items())
for key,value in dic.items():
    print(key,"\t",value)
'''
'''
# 예제.11
dic={1:'a',2:'b',3:'c'}
print(dic)
a=dic.pop(2)
print(dic,a)
b=dic.popitem() #아무것도 지정하지 않으면 마지막에 있는 값을 삭제
#아무것도 지정하지 않고 써야함
print(dic,b) #popitem은 키와 값을 튜플로 반환함
dic.clear()
print(dic)
'''

# 사전 자료형 복사 예제.1
'''
# 얇은복사

import copy
info = {1:"일",2:"이",3:"삼"}
info2 = info
print(info, id(info))
print(info2, id(info2))
info2[1]="TEST"
print(info, id(info))
print(info2, id(info2))
'''
'''
#깊은복사

import copy
info = {1:"일",2:"이",3:"삼"}
info2 = copy.copy(info)
print(info, id(info))
print(info2, id(info2))
info2[1]="TEST"
print(info, id(info))
print(info2, id(info2))
'''

# 사전 자료형 복사 예제.2
import copy
lst = [1,2,3,4]
info = {}
info["Data"]=copy.copy(lst)
print(lst,id(lst))
print(info["Data"],id(info["Data"]))

lst[0] = 100
print(lst,id(lst))
print(info["Data"],id(info["Data"]))