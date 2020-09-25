'''
1. 구구단을 출력하세요. continue, break, if X

i=2
while i<10:
    j=1
    while i >= j:
        print("{} x {} = {}".format(i, j, i*j))
        j+=1
    i+=2
    print()

2. 10~20 사이의 수를 입력 받아서 1부터 입력받은 수까지의 합을 구하세요.

i=1
Sum=0

while True:
    num = int(input("10-20 사이의 숫자 입력: "))
    if num>=10 and num<=20:
        break
    print("잘못 입력하셨습니다..")

while i<=num:
    Sum += i
    i+=1
print("1~{} 까지의 합: {}".format(num, Sum))

3. 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한마리가 하루에 20g씩 쌀을 먹고,
 10일마다 마리 수가 2배씩 증가한다. 며칠만에 창고의 쌀이 모두 쥐에 먹이가 될까?
 그리고 쥐는 총 몇 마리인가?(쌀 한통=1kg)

 rice=100000
mouse=2
day=1

while rice > 0:
    rice -= mouse*20
    if day%10 == 0:
        mouse *= 2
    print(day,"일\t",mouse,"마리\t",rice,"g")
    day += 1



# 반복문 중첩(for문 -> while문)

i=0
while i<3:
    j=0
    while j<5:
        if j==3:
            break
        print("i: {}, j: {}".format(i, j))
        j+=1
    i+=1





# 자판기 프로그램 제작하기

money = int(input("요금을 투입하세요: "))

while True:
    print("======자판기 프로그램=======")
    print("1.커피(200)\t2.코코아(250)\t3.반환\t4.종료\n")
    menu = int(input("메뉴를 선택하세요: "))

    if ((menu==1 and money<200) or (menu==2 and money<250)):
        print("요금이 부족합니다...")
    elif menu==1:
        print("커피 맛있게 드세요.")
        money -= 200
    elif menu==2:
        print("코코아 맛있게 드세요.")
        money -= 250
    elif menu==3:
        print("반환 금액: ", money)
        money=0
    elif menu==4:
        break
    else:
        print("잘못 입력했습니다...")
 



 #별찍기

 * * * * *
 * * * * *
 * * * * *
 * * * * *
 * * * * *  

i=0
while i<5:
    j=1
    while j<5:
        print("* ", end='') 
        j+=1
    print()
    i+=1

 * * * * *
 * * * * 
 * * *
 * *
 *  

i=0
while i<5:
    j=i
    while j<5:
        print("* ", end='') 
        j+=1
    print()
    i+=1

* * * * *
  * * *
    *
'''

for 3: #행
    for :#공백
    for :#값


