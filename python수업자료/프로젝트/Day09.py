# for i in range(1, 10, 1):
#     for j in range(2, 10, 1):
#         print("{} x {} = {}".format(j, i, i*j), end='\t')
#     print()


# for i in range(0, 5, 1):
#     print("상위for문 {}일 때, 하위 for문".format(i), end=':')
#     for j in range(0, 5, 1):
#         print(i*j, end=' ')
#     print()


# for i in range(0, 5, 1):
#     for j in range(1, 6, 1):
#         print(j+5*i, end='\t')
#     print()

# while문
# i=0         #초기식
# while i<5:  #조건식
#     print("hello world")
#     i+=1    #증감식

# i=1
# even, odd = 0, 0
# while i<=10:
#     if i%2 == 0:
#         even += i
#     else:
#         odd += i
#     i+=1
# print("1-10 짝수의 합: ", even)
# print("1-10 홀수의 합: ", odd)

# i=0
# while i<5:
#     print(i)
#     i+=1
# #while 문 안에 i가 4일때까지 i+=1을 실행한 후에는
# #else문에서 i값은 5가 된다.
# else:
#     print(i)

# i=1
# flag = True
# while flag:
#     print(i)
#     if i==10:#여기에 flag 조건이 False가 없으면 계속 무한루프를 돌게된다.
#         flag = False
#     i+=1

# break, continue
# i=0
# while True:
#     if i==3:
#         break
#         print("3 출력")
       
#     print(i, "출력")
#     i+=1
# print("다음 문장")


# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#         print("3출력")
#     print(i, "출력")
# print("다음 문장")


# 구구단을 출력하세요. 짝수단만, 2단은 2*2까지만, 4단은 4*4까지만, 6단은 6*6까지만, 
# break, continue를 사용해서 문제를 해결하세요.

i=1
j=1
while i<10:
    i+=1
    if i%2==1:
        continue
    j=1
    while j<10:
        print("{} x {} = {}".format(i,j,i*j))
        j+=1
        if j>i:
            break    
    print()
    