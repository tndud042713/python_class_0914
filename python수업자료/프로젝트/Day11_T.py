'''
# [예제.1]
from random import random
print(random())              # 0.0 ~ 1.0 사이의 임의의 값 생성 후 출력
print(random() * 10)         # 0.0 ~ 10.0 사이의 임의의 값 생성 후 출력
print(random() * 50)         # 0.0 ~ 50.0 사이의 임의의 값 생성 후 출력
print(int(random() * 5) + 1) # 1 ~ 5 사이의 임의의 값 생성 후 출력

for x in range(5):
    print(int(random()*10) + 1)

from random import random
# 1 ~ 100사이에 짝수의 임의의 값 생성
print((int(random() * 50) + 1) * 2)

# 1 ~ 100사이에 홀수의 임의의 값 생성
print((int(random() * 50) + 1) * 2 - 1)
'''
# # [문제.1]
# from random import random
# for i in range(6):
#     print(int(random() * 100) + 1)

# # [문제.2]
# from random import random
# while True:
#     rand = (int(random() * 100) + 1)
#     print(rand)
#     if rand == 50:
#         print("반복종료!")
#         break

# # [문제.3]
# from random import random
# while True:
#     rand1 = (int(random() * 15) + 1)
#     rand2 = (int(random() * 15) + 1)
#     rand3 = (int(random() * 15) + 1)
#     if rand1 != rand2 and rand1 != rand3 and rand2 != rand3:
#         print(rand1, rand2, rand3)
#         break

# from random import random, randrange, randint
# print(randrange(0,100,2))
# print(randrange(1,100,2))
# print(randint(1,10))


# [ List 사용 하기 ]
# : 리스트는 (List) 데이터의 목록을 다루는 자료 형.
# : 리스트를 정의 할 때에는 [ ] (대괄호)를 사용 한다.
# : 리스트 안에는 어떠한 자료 형이든지 넣어 사용 할 수 있다.


# #[예제.2]
# lst = [1,2,3]
# print(lst, type(lst))
# print(lst[0])
# print(lst[1])
# print(lst[2])

# lst = [100,"String", 123.456]
# print(lst, type(lst))
# print(lst[0], type(lst[0]))
# print(lst[1], type(lst[1]))
# print(lst[2], type(lst[2]))

# # [예제.3]
# lst = [1,2,3]
# print(lst, type(lst))
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])

# [예제.4]
# a = [0,0,0,"합계"]
# for i in range(len(a)-1):
#     a[i] = int(input("정수입력: "))
# Sum = a[0] + a[1] + a[2]
# print("{} : {}".format(a[3],Sum))

# [예제.5]
# lst = [10,20,30,40,50]
# print(lst)
# print(lst[1:3])
# print(lst[2:4])
# print(lst[3:])
# print(lst[:2])
# print(lst[-5:-3])

# # [ "List" 복사 ]
# # : 얇은 복사 , 깊은 복사 2가지 종류의 복사가 있다.
# # : 얇은 복사는 [원본 List]의 주소 값을 [사본 List]에 적용하는 형태의 복사 
# # : ( 즉, 주소 값만 복사하는 형태를 말한다. )
# # : 얇은 복사는 쉽게, 기존의 List에 또 다른 이름이 부여 되는 것이다.

# # [EX] : 얇은 복사 (바로가기 만들기)
# # lst1 = [1,2,3,4,5]
# # lst2 = lst1

# # : 깊은 복사는 [원본 List]의 주소 값을 복사하는 것이 아닌 새로운 [사본 List]를 생성하여 데이터를 복사한다.
# # : 일반적으로 우리가 사용하는 형식의 복사라고 생각하면 된다. 
# # : 단, Import를 이용하여 copy 기능을 불러와서 사용해야 한다.

# # [EX] : 깊은 복사 
# # import copy
# # lst1 = [1,2,3,4,5]
# # lst2 = copy.copy(lst1)


# # [예제.6] : 얇은 복사
# lst1 = [1,2,3,4,5]
# lst2 = lst1
# lst2[0] = 100
# print("lst1[0]:",lst1[0])
# print("lst2[0]:",lst2[0])
# print(id(lst1), id(lst2))

# # [예제.7] : 깊은 복사
# import copy
# lst1 = [1,2,3,4,5]
# lst2 = copy.copy(lst1)
# lst2[0] = 100
# print("lst1[0]:",lst1[0])
# print("lst2[0]:",lst2[0])
# print(id(lst1), id(lst2))
# '''


