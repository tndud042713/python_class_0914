'''
[ Quiz 1 ] : 중첩 For문을 이용하여 구구단을 구현하세요.

for i in range(1, 10, 1):
    for j in range(2, 10, 1):
        print("{} x {} = {}".format(j, i, i*j), end='\t')
    print()

[ Quiz 2 ]: 아래와 같이 출력하세요.
상위포문0 일때 하위포문:0 0 0 0 0
상위포문1 일때 하위포문:0 1 2 3 4
상위포문2 일때 하위포문:0 2 4 6 8
상위포문3 일때 하위포문:0 3 6 9 12
상위포문4 일때 하위포문:0 4 8 12 16

for i in range(0, 5, 1):
    print("상위for문 {}일 때, 하위 for문".format(i), end=':')
    for j in range(0, 5, 1):
        print(i*j, end=' ')
    print()

[ Quiz 3 ]: 이중 for문을 이용하여 아래와 같이 출력하시오.
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25

for i in range(0, 5, 1):
    for j in range(1, 6, 1):
        print(j+5*i, end='\t')
    print()


#반복문(while)
i=0         #초기식
while i<5:  #조건식
    print("hello world")
    i+=1    #증감식


# 1-10 짝수의 합, 홀수의 합
i=1
even, odd = 0, 0
while i<=10:
    if i%2 == 0:
        even += i
    else:
        odd += i
    i+=1
print("1-10 짝수의 합: ", even)
print("1-10 홀수의 합: ", odd)



#while~else
i=0
while i<5:
    print(i)
    i+=1
else:
    print(i)




#무한루프
i=1
flag = True
while flag:
    print(i)
    if i==10:
        flag = False
    i+=1






# break, continue

i=0
while True:
    if i==3:
        break
        print("3출력")
    print(i, "출력")
    i+=1
print("다음 문장")



i=0
while i<5:
    i+=1
    if i==3:
        continue
        print("3출력")
    print(i, "출력")
print("다음 문장")
'''

# 구구단을 출력하세요. 짝수단만, 2단은 2*2까지만, 4단은 4*4까지만, 6단은 6*6까지만, 
# break, continue를 사용해서 문제를 해결하세요.

i=1
while i<10:
    
    if i%2 != 0:
        continue
    j=1
    while j<10:
        if i<j:
            break
        print("{}x{}={}".format(i, j, i*j))
        j+=1
    print()
    i+=1
