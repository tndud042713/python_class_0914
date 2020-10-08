'''
import os
menu = {}
flag = True
while flag:
    print("=" * 20) # *20개출력
    print("1. 메뉴 등록")
    print("2. 메뉴 출력")
    print("3. 메뉴 가격 수정")
    print("4. 프로그램 종료")
    print("=" *20)
    num = int(input("번호선택>> "))
    if num==1:
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
    os.system("pause")
    os.system("cls")
'''
'''
[Quiz.1] : 주소 등록 프로그램 제작
1.주소 등록
2.주소 수정
3.주소 목록
4.주소 검색
5.프로그램 종료
'''
