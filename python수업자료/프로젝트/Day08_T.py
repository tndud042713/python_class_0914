
'''
[Quiz 1]
1. 1~10까지의 합을 구하세요. 단, 반복문을 이용하세요.

Sum = 0
for i in range(1, 11, 1):
    Sum += i
print("1부터 10까지의 합은 {}입니다.".format(Sum))



2. For문과 IF문을 이용하여 아래와 같이 출력.
힌트 : 5번 출력하고 줄 바꿈이 이루어져야 하므로, 5의 배수마다 줄 바꿈 처리하도록 조건을 설정한다.
1     2       3       4       5   
6     7       8       9      10      
11   12      13      14      15      
16   17      18      19      20      
21   22      23      24      25      
26   27      28      29      30 



for i in range(1, 31, 1):
    print(i, end='\t')
    if i % 5 == 0:
        print()


3. 변수 st = 'It is a fun Python class' 다음 문자열 중에서 
알파벳 ‘a’의 개수와 ‘s’의 개수를 구하시오.


st = 'It is a fun Python class'
acnt = scnt = 0

for i in st:
    if i == 'a':
        acnt += 1
    if i == 's':
        scnt += 1
print("a의 개수: {}, s의 개수: {}".format(acnt, scnt))


#[ Quiz.2 ]
1. 수를 입력 받아 1 ~ 입력 받은 수 까지 짝수의 합과 홀수의 합을 출력

evenSum,  oddSum = 0, 0
num = int(input("입력: "))

for i in range(1, num+1, 1):
    if i%2 == 0:    #짝수라면
        evenSum += i
    else:           #홀수라면
        oddSum += i
print("짝수의 합: {}".format(evenSum))
print("홀수의 합: {}".format(oddSum))

2. 시작 값, 끝 값, 증가값(1) 입력받아 시작과 끝값 사이의 7의 배수를 출력 하시오.

s = int(input("시작값: "))
e = int(input("끝값: "))

for i in range(s, e+1, 1):
    if i%7 == 0:
        print(i, end=' ')

3. 1 ~ 100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.

Sum = 0
for i in range(1, 101, 1):
    if i%3==0 and i%5==0:
        Sum += i
print(Sum)

4. 두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오.

Sum = 0
n1 = int(input("입력1: "))
n2 = int(input("입력2: "))

if n1 < n2:
    for i in range(n1, n2+1, 1):
        Sum += i
if n1 > n2:
    for i in range(n2, n1+1, 1):
        Sum += i
        
print(Sum)




for i in range (9,1,-1):    #9~2, 1씩 감소
    for j in range (9,0,-1):    #9~1, 1씩 감소
        print('{} X {} = {}\t'.format(i,j,i*j))
    print()



[ Quiz 1 ] : 중첩 For문을 이용하여 구구단을 구현하세요.

[ Quiz 2 ]: 아래와같이출력되게만드시오.
상위포문0 일때하위포문:0 0 0 0 0
상위포문1 일때하위포문:0 1 2 3 4
상위포문2 일때하위포문:0 2 4 6 8
상위포문3 일때하위포문:0 3 6 9 12
상위포문4 일때하위포문:0 4 8 12 16

[ Quiz 3 ]: 이중 for문을이용하여 아래와 같이 출력하시오.
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
'''