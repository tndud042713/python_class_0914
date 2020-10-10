'''
# [종합 예제.1] : 메뉴 등록 프로그램
import os
menu = {}
flag = True
while flag:
    print("=" * 20)
    print("1. 메뉴 등록")
    print("2. 메뉴 출력")
    print("3. 메뉴 가격 수정")
    print("4. 프로그램 종료")
    print("=" * 20)
    num = int(input("번호선택 >> "))
    if num == 1:
        name = input("메뉴 이름: ")
        if menu.get(name) == None:
            menu[name] = input("메뉴 가격: ")
        else:
            print("입력하신 메뉴는 이미 존재합니다.")
    elif num == 2:
        for key, val in menu.items():
            print(key,"\t",val)
    elif num == 3:
        name = input("수정하실 메뉴 이름: ")
        if menu.get(name) == None:
            print("입력하신 메뉴는 존재하지 않습니다.")
        else:
            menu[name] = input("수정 가격 입력: ")
    elif num == 4:
        flag = False
        print("프로그램을 종료 합니다.")
    else:
        print("번호를 다시 선택하세요!")
    os.system("pause") #커멘드창이 안 닫히게 하는 코드이다
    os.system("cls") # 콘솔창을 지우고 깔끔하게 쓰고싶을 때 사용하는 코드이다
'''
'''
[Quiz.1] : 주소 등록 프로그램 제작
1.주소 등록
2.주소 수정
3.주소 목록
4.주소 검색
5.프로그램 종료
'''
'''
import os
addr = {}
flag = True
while flag:
    print("=" * 20)
    print("1. 주소 등록")
    print("2. 주소 수정")
    print("3. 주소 목록")
    print("4. 주소 검색")
    print("5. 프로그램 종료")
    print("=" * 20)
    num = int(input("번호선택 >> "))
    if num == 1:
        name = input("목적지 이름: ")
        if addr.get(name) == None:
            addr[name] = input("목적지 주소: ")
        else:
            print("입력하신 메뉴는 이미 존재합니다.")
    elif num == 2:
        name = input("수정하실 목적지 이름: ")
        if addr.get(name) == None:
            print("해당 목적지는 존재하지 않습니다.")
        else:
            addr[name] = input("수정하실 목적지 주소 입력: ")
    elif num == 3:
        for key, val in addr.items():
            print(key,"\t",val)
    elif num == 4:
        name = input("검색하실 목적지 이름: ")
        if addr.get(name) == None:
            print("해당 목적지는 존재하지 않습니다.")
        else:
            print(name,"\t",addr.get(name))
    elif num == 5:
        flag = False
        print("프로그램을 종료 합니다.")
    else:
        print("번호를 다시 선택하세요!")
    os.system("pause")
    os.system("cls")
'''
'''
# [종합 예제.2] : 일정 등록 프로그램
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








# [ 학생정보등록 프로그램 정답코드 ]
import os,copy,collections
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
            if val not in info[number].keys():
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

