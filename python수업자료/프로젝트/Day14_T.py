'''
1.여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력 하시오. (5개 값 저장)
( Tuple의 값을 리스트에 저장하시오. 단, Len 함수를 이용) 

2.아래와 같이 출력 시키시오
-----------------------------------
     (Tuple)          (List)
    회사정보     :   삼성전자
    제품명       :    Galaxy
    가격정보     :    100원
    출시일       :    미정
-----------------------------------

3.위에서 출력 한 내용을 업데이트 하시오. [ 단, Index, Insert, Remove 함수를 전부 사용할 것 ]
가 격 : 100 -> 110
출시일 : 미정 -> 이번 달 말

#[문제.1]
tu = (10,20,"Tuple","Test",111.222)
for i in range(len(tu)):
    print("Data:",tu[i])
#for i in tu:
#    print("Data:",i)

#[문제.2]
tu = ("회사정보","제품명","가격정보","출시일")
ls = ["삼성전자","Galaxy","100원","미정"]
print("---------------------------------------")
print("(Tuple)\t\t\t(List)")
for i in range(len(tu)):
    print("{:10}\t:\t{}".format(tu[i],ls[i]))
print("---------------------------------------")

#[문제.3]
tu = ("회사정보","제품명","가격정보","출시일")
ls = ["삼성전자","Galaxy","100원","미정"]
a = ls.index("100원")
b = ls.index("미정")
ls.remove("100원")
ls.remove("미정")
ls.insert(a,"110원")
ls.insert(b,"이번달말")
print("---------------------------------------")
print("(Tuple)\t\t\t(List)")
for i in range(len(tu)):
    print("{:10}\t:\t{}".format(tu[i],ls[i]))
print("---------------------------------------")

[ Dictionary ] # -> {KEY1:[Value1,Value2,Value3], KEY2:[Value1,Value2,Value3]}
: List와 비슷하다, List와 같이 첨자를 이용하여 요소에 접근 한다.
: Dictionary의 첨자는 Key를 사용 한다.
: Key가 가리키는 곳에 데이터를 저장.
: 탐색 속도가 빠르고, 사용하기 편리하다.
: Dictionary 정의 시 " { } "를 이용한다. 
: 특정 슬롯에 새로운 Key-Value를 입력하거나 Dictionary 안에 있는 요소를 참조 할 때에는 "[KEY]"를 사용.

# [예제.1]
student = {"학번":"00-1234", "이름":"홍길동", "학과":"컴퓨터공학"}
print(student,type(student))
print(student["학번"])
print(student["이름"])
print(student["학과"])

# [예제.2]
www = {}
www["파이썬"] = "www.python.org"
www["네이버"] = "www.naver.com"
www["구글"] = "www.google.com"
print(www,type(www))
print(www["파이썬"], type(www["파이썬"]))
print(www["네이버"], type(www["네이버"]))
print(www["구글"], type(www["구글"]))

# [예제.3]
info = {}
key = input("키 값 입력: ")
val = int(input("정수 값 데이터 입력: "))
info[key] = val
print(info)

# [예제.4]
info = {}
lst = [1,2,3,4,5]
tu = (6,7,8,9,10)
info["테스트"] = lst
info["파이썬"] = tu
print(info)
print(info["테스트"])
print(info["파이썬"])

[ Dictionary 문제 ]
Key값과 Value값을 입력 받아 저장 후 출력 하시오.
이름(key) 입력 : 겐지
값(value) 입력 : 수리검
이름(key) 입력 : 맥크리
값(value) 입력 : 섬광탄
이름(key) 입력 : 파라
값(value) 입력 : 로켓런처
이름(key) 입력 : 리퍼
값(value) 입력 : 샷건
이름(key) 입력 : 솔저
값(value) 입력 : 나선로켓

* 출력 예시 *
{'솔저': '나선로켓', '맥크리': '섬광탄', '리퍼': '샷건', '파라': '로켓런처', '겐지': '수리검'}

over = {}
for i in range(5):
    k = input("이름(key) 입력: ")
    v = input("값(value) 입력: ")
    over[k] = v
print(over)

# [예제.5]
dic = {1:'a',2:'b',3:'c'}
print(dic)
dic.update({4:'d'})
print(dic)

# [예제.6]
dic = {1:'a',2:'b',3:'c'}
print(dic)
print(dic.get(1)) 
print(dic.get(2))
print(dic.get(3))
print(dic.get(4))
if dic.get(4) == None:
    print("해당 키값은 존재하지 않습니다.")

# [예제.7]
key_list = [1,2,3,4,5]
dic1 = {}.fromkeys(key_list)
dic2 = {}.fromkeys(key_list,'a')
print(dic1)
print(dic2)

# [예제.8]
dic = {1:'a',2:'b',3:'c'}
print(dic.keys())
print(dic.values())
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic)) # 기본값으로 키값을 반환

# [예제.9]
sub = {}
sub["과목명"] = input("과목이름 입력: ")
sub["수업시간"] = int(input("수업시간 입력: "))
print()
for i in sub:
    print("{} : {}".format(i,sub[i]))

# [예제.10]
dic = {1:'a',2:'b',3:'c'}
print(dic)
print(dic.items())
for key, value in dic.items():
    print(key,"\t",value)

# [예제.11]
dic = {1:'a',2:'b',3:'c'}
print(dic)
a = dic.pop(2)
print(dic, a)
b = dic.popitem()
print(dic,b)
dic.clear()
print(dic)

# [사전 자료형 복사 예제.1]
import copy
info = {1:"일", 2:"이", 3:"삼"}
info2 = copy.copy(info)
print(info, id(info))
print(info2, id(info2))
info2[1] = "TEST"
print(info, id(info))
print(info2, id(info2))

# [사전 자료형 복사 예제.2] : List + Dic
import copy
lst = [1,2,3,4]
info = {}
info["Data"] = copy.copy(lst)
print(lst,id(lst))
print(info["Data"],id(info["Data"]))

lst[0] = 100
print(lst,id(lst))
print(info["Data"], id(info["Data"]))
'''







