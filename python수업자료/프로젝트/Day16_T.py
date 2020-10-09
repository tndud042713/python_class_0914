'''
# [ 학생정보등록 프로그램 정답코드 ]
import os, copy, collections
info = {}; info2 = collections.OrderedDict()
wh=True; num=0; number = ""; name = ""; addr = ""; gr = ""
while wh:
    print("===============================")
    print("1.학생 등록");print("2.학생 검색")
    print("3.학생 수정");print("4.학생 삭제")
    print("5.전체 학생 목록");print("6.종료")
    print("===============================")
    num = int(input("번호 선택 >> "))
    if num == 1:
        number = input("학번 입력: ")
        if info.get(number) == None:
            name = input("학생 이름 입력: ")
            addr = input("학생 주소 입력: ")
            gr = input("학생 등급 입력: ")
            info2["학번"]=number; info2["이름"]=name; info2["주소"]=addr; info2["등급"]=gr
            info[number] = copy.deepcopy(info2)
            # {"100-1":{"학번":"100-1","이름":"홍길동","주소":"서울시","등급":"A"},"100-2":{"학번":"100-2","이름":"이순신","주소":"경기도","등급":"A"}}
            info2.clear()
            print("등록 완료")    
        else:
            print("이미 등록 된 학번 입니다.")

    elif num == 2:
        number = input("검색 학번 입력: ")
        if info.get(number) == None:
            print("입력 하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {}입니다.".format(number,info[number]))

    elif num == 3:
        number = input("수정 하실 학번 입력: ")
        if info.get(number) == None:
            print("입력하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {} 입니다.".format(number,info[number]))
            val = input("수정 항목 입력: ")
            # {"100-2":{"학번":"100-2","이름":"홍길동","주소":"서울시","등급":"A"}}
            if val not in info[number].keys(): # Data Group -> ("학번", "이름", "주소", "등급")
                print("수정 항목을 확인해주세요.")
                print("메뉴선택 화면으로 돌아갑니다.")
                os.system("pause")
                os.system("cls")
                continue
            change = input("변경 정보 입력: ")
            if val == "학번":
                if info.get(change) == None:
                    info[number][val] = change
                    tmp = info[number]
                    info.pop(number)
                    info.update({change:tmp})
                    print("수정 완료")
                else:
                    print("이미 등록 된 학번 입니다.")
            else:
                info[number][val] = change
                print("수정 완료")

    elif num == 4:
        number = input("삭제 하실 학번입력:")
        if info.get(number) == None:
            print("입력하신 학번은 존재하지 않습니다.")
        else:
            print("학번 {}의 정보는 {}입니다.".format(number,info[number]))
            info.pop(number)
            print("삭제완료")
            
    elif num == 5:
        for k,v in info.items():
            print(k,"\t",v)

    elif num == 6:
        wh = False
        print("프로그램 종료")

    else:
        print("번호를 잘 못 선택하셨습니다.")

    os.system("pause")
    os.system("cls")

# [예제.1]
Str = "String Indexing"
print(Str[0])
print(Str[3])
print(Str[8])

Str2 = "String Slicing"
print(Str2[:6])
print(Str2[7:])

for val in Str:
    print(val,end="")
print()

Str3 = Str + Str2
print(Str3)
Str3 = Str + " " + Str2
print(Str3)
print(Str3 * 3)

# [예제.2]
Str = "python is easy. programming test"
print(Str)
Str = Str.upper()
print(Str)
Str = Str.lower()
print(Str)
Str = Str.title()
print(Str)
Str = Str.swapcase()
print(Str)

# [예제.3]
st = "Have a nice day"
print(st)
print(st.count("a"))
print(st.count("day"))
print(st.count("dak"))

cnt_a = 0
for i in st:
    if i == 'a':
        cnt_a += 1
print(cnt_a)

# [예제.4]
st = "Have a nice day"
print(st)
print(st.find("day"))
print(st.find("dak"))
print(st.index("day"))
print(st.index("dak"))

st = "Have a nice day"
print(st.find('a'))
print(st.find('a',2))
print(st.find('a',6))
print(st.find('a',14))

[ Quiz ] : List 정의 하여 첨자 위치 저장
a의 총 개수와 첨자의 위치를 출력 하시오
st = 'Have a nice day Have a nice day Have a nice day'

[ 출력 결과 ]
a 개수 : 9
첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]

st = 'Have a nice day Have a nice day Have a nice day'
cnt = 0
ls = []
for i in st:
    cnt = st.find('a',cnt)
    if cnt != -1:
        ls.append(cnt)
        cnt+=1
print("a 개수: ",st.count('a'))
print("첨자: ",ls)

# [예제.5]
st = " 파이썬 "
print("{}{}{}".format("*",st,"*"))
print("{}{}{}".format("*",st.strip(),"*"))
st = st.strip()
print(st)

st = "파이썬파"
print(st)
print(st.strip("파"))
print(st.lstrip("파"))
print(st.rstrip("파"))

# [예제.6]
st = "2020/10/08"
print(st)
print(st.replace('/',"."))
print(st.replace(st[:4],"2021"))

# [예제.7]
st = """Have a nice day
Have a nice day
Have a nice day"""
print(st)

[ Quiz.2 ] : replace의 활용, ":" 첨자를 구하여 Slicing 활용
st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월14일"""

- 위의 내용을 아래와 같이 변경 하시오 
- "–(바)" -> ":(콜론으로 변경)", 년도를 1999년으로 모두 변경 

[결과]
김개똥 :1999년 03월 24일
홍길동구리 :1999년 04월 02일
선우선녀 :1999년 05월14일

st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월14일"""

st = st.replace('-',":")
i = 0
for k in range(st.count(":")):
    i = st.find(":", i + 1)
    st = st.replace(st[i+1:i+5],"1999")
print(st)
'''
