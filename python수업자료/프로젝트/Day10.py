# i=2
# while i<10:
#     j=1
#     while i>=j:
#         print("{}x{}={}".format(i, j, i*j))
#         j+=1
#     i+=2
#     print()

# i=1
# Sum=0;
# while True:
#     num = int(input("10-20 사이의 숫자 입력: "))
#     if num>=10 and num<=20:
#         break
#     print("잘못 입력하셨습니다. 다시 입력하세요")

# while i<=num:
#     Sum+=i
#     i+=1
# print("01~{} 까지의 합: {}".format(num,Sum))

# rice = 100000
# mouse = 2
# day =1

# while rice > 0:
#     rice -= mouse*20
#     if day%10 == 0:
#         mouse *=2
#     print(day,"일\t",mouse,"마리\t",rice,"g")
#     day +=1

# 반복 중첩
# for i in range(0,3,1):
#     for j in range(0,5,1):
#         if j==3:
#             break
#         print("i: {}, j: {}".format(i,j))

# i=0
# while i<3:
#     j=0
#     while j<5:
#         if j==3:
#             break
#         print("i: {}, j: {}".format(i,j))
#         j+=1
#     i+=1


# # 자판기

# money=int(input("요금을 투입 하세요: "))

# while True:
#     print("========커피 자판기=========")
#     print("1. 커피<200>  2. 코코아<250>  3. 반환 4. 종료")
#     print(f"현재 남은 요금{money}원")
#     menu = int(input("메뉴를 선택하세요: "))
    

#     if ((menu==1 and money<200) or (menu==2 and money<250)):
#         print("요금이 부족합니다...")
#         print("반환금액: ",money)
#         money=0
#     elif menu==1:
#         print("커피 맛있게 드세요.")
#         money=money-200
#     elif menu==2:
#         print("코코아 맛있게 드세요.")
#         money=money-250
#     elif menu==3:
#         print("반환금액: ",money)
#         money=0
#     elif menu==4:
#         break
#     else:
#         print("잘못 입력했습니다...")

# 별짓기


# for i in range(0,5,1):
#     for j in range(0,5,1):
#         print("★",end=" ")
#     print()
# print()

# for i in range(0,5,1):
#     for j in range(i,5,1):
#         print("★",end=" ")
#     print()
# print()

for i in range(0,3,1):
    for j in range(0,i,1):
        print(end="  ")
    for k in range(0,5-2*i,1):
        print("* ",end="")
    print()