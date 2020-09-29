'''
# [예제.1]
lst = [1,2,3]
print("첫 번째 출력:",lst)
lst.append('a')
print("두 번째 출력:",lst)
lst.append([100,200])
print("세 번째 출력:",lst)

# [예제.2]
lst = [1,2,3]
print("첫 번째 출력:",lst)
lst.extend(['a','b','c'])
print("두 번째 출력:",lst)

# [예제.3]
lst = [1,2,3]
print("첫 번째 출력:",lst)
lst.insert(1,'a')
print("두 번째 출력:",lst)

#[예제.4]
lst = [1,2,3]; lst2 = ['a','b','c']
print("첫 번째 출력:",lst)
lst.pop()
print("두 번째 출력:",lst)
num = lst.pop(0)
print("세 번째 출력:",lst)
print(num)
lst2.append(lst.pop())
print("네 번째 출력:",lst)
print(lst2)

#[예제.5]
lst = [1,2,3]
print("첫 번째 출력:",lst)
num = lst.remove(2)
print("두 번째 출력:",lst)
print(num)
lst.clear()
print("세 번째 출력:",lst)

lst = [1,2,3]
lst2 = lst # 얇은복사
lst2.clear()
print(lst)

#[예제.6]
lst = [1,2,3,4,5,1]
print(lst)
print(lst.count(1))
print(lst.index(3))
lst.reverse()
print(lst)

#[예제.7]
lst = [78,12,34,56,80]
print("정렬전 데이터 출력:",lst)
lst.sort()
print("오름차순 정렬 후 데이터 출력:", lst)
lst.sort(reverse=True)
print("내림차순 정렬 후 데이터 출력:", lst)

# [ Quiz 1 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 아래와 같이 출력 되도록 코드를 작성하세요.
현재 리스트 : [30, 20, 10]
append(40) 후의 리스트 : [30, 20, 10, 40]
pop() 으로 추출한 값 : 40
pop() 후의 리스트 : [30, 20, 10]
sort() 후의 리스트 : [10, 20, 30]
reverse() 후의 리스트 : [30, 20, 10]

# [ Quiz 1 정답 코드 ]
List = [ 30 , 20 ,10 ]
print('현재 리스트 : {}'.format(List))
List.append(40)
print('append(40) 후의 리스트 : {}'.format(List))
print('pop() 으로 추출한 값 : {}' .format(List.pop()))
print('pop() 후의 리스트 : {}' .format(List))
List.sort()
print('sort() 후의 리스트 : {}' .format(List))
List.reverse()
print('reverse() 후의 리스트 : {}' .format(List))

# [ Quiz 2 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 아래와 같이 출력 되도록 코드를 작성하세요.
현재 리스트 : [30, 20, 10]
10 값의 위치 : 2
insert(2,200) 후의 리스트 : [30, 20, 200, 10]
remove(200) 후의 리스트 : [30, 20, 10]
extend( [ 555 , 666 , 555 ] ) 후의 리스트 : [30, 20, 10, 555, 666, 555]
555 값의 개수 : 2

# [ Quiz 2 정답 코드 ]
List = [ 30 , 20 ,10 ]
print('현재 리스트 : {}'.format(List))
print('10 값의 위치 : {}'.format(List.index(10)))
List.insert(2,200)
print('insert(2,200) 후의 리스트 : {}'.format(List))
List.remove(200)
print('remove(200) 후의 리스트 : {}'.format(List))
List.extend( [ 555 , 666 , 555 ] )
print('extend( [ 555 , 666 , 555 ] ) 후의 리스트 : {}'.format(List))
print('555 값의 개수 : {}'.format(List.count(555)))

#[예제.8]
lst = [100,200,300,400]
for i in lst:
    print(i)

for i in range(len(lst)):
    print(i)

#[예제.9] : 2차원 리스트
aa = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]
print(aa)
print()
print(aa[0])
print(aa[1])
print(aa[2])
print()
print(aa[0][0])
print(aa[0][1])
print(aa[0][2])

aa = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]
for i in range(3):
    for j in range(4):
        print(aa[i][j],end="\t")
    print()
'''
# [Quiz] : 코드해석 실습
ls_1 = []; ls_2 = []; value = 1
for i in range(0,3):
    for k in range(0,4):
        ls_1.append(value)
        value+=1
    ls_2.append(ls_1)
    ls_1=[]
for i in range(0,3):
    for k in range(0,4):
        print('{}\t'.format(ls_2[i][k]),end='')
    print()
print('ls_2 : {}'.format(ls_2))






