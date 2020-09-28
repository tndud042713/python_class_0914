# 예제.1
# from random import random
# print(random()) #0.0 ~ 1.0  사이의 임의의 값 생성 후 출력
# print(random()*10) #0.0 ~ 10.0  사이의 임의의 값 생성 후 출력
# print(random()*50) #0.0 ~ 50.0  사이의 임의의 값 생성 후 출력
# print(int(random()*30)) #0 ~ 30 사이의 임의의 값 생성 후 출력
# print(int(random()*5)+1) #1 ~ 5 사이의 임의의 값 생성 후 출력

# for x in range(5):
#     print(int(random()*10)+1)

# #1 ~ 100사이에 짝수의 임의의 값 생성
# print((int(random()*50)+1)*2)
# #1 ~ 100사이에 홀수의 임의의 값 생성
# print((int(random()*50)+1)*2-1)

# pdf연습문제
# from random import random
# for x in range(6):
#     print(int(random()*100)+1)

# from random import random
# while True:
#     a=int(random()*100)+1
#     print(a)
#     if a==50:
#         print(a,"는 50 이므로 탈출합니다")
#         break
    


# 3번은 못풀었으므로 강사 풀이 참조
# 괜히 더 큰 경우를 생각했다가 풀지 못했다...
# from random import random
# while True:
#     rand1 = (int(random()*15)+1)
#     rand2 = (int(random()*15)+1)
#     rand3 = (int(random()*15)+1)
#     if rand1 != rand2 and rand1 != rand3 and rand2 != rand3:
#         print(rand1,rand2,rand3)
#         break

# from random import random,randrange,randint
# print(randrange(2,100,2))
# print(randrange(1,100,2))
# print(randint(1,10))

# [List 사용하기]
# 예제.2
# lst = [1,2,3]
# print(lst,type(lst))
# print(lst[0])
# print(lst[1])
# print(lst[2])
# # print(lst[3])

# lst = [100,"String",123.456]
# print(lst,type(lst))
# print(lst[0],type(lst[0]))
# print(lst[1],type(lst[1]))
# print(lst[2],type(lst[2]))

# 예제.3
# 인덱스를 음수값으로 줄 수도 있다
# lst = [1,2,3]
# print(lst,type(lst))
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])

# 예제.4
# 리스트를 이용해서 관리하면 변수의 이름에 따라 하나로 관리할 수 있어서
# 효과적이다
# a=[0,0,0,"합계"]
# a[0] = int(input("첫 번째 정수입력: "))
# a[1] = int(input("첫 번째 정수입력: "))
# a[2] = int(input("첫 번째 정수입력: "))
# for i in range(len(a)-1): # len함수를 이용하면 배열의 값만큼만 이용가능
# # 여기서는 마지막 요소가 "합계"라는 스트링 값으로 들어가기 때문에 -1 해준다
#     a[i]=int(input("{}번째 정수입력 : ".format(i+1)))
# Sum = a[0]+a[1]+a[2]
# print("{} : {}".format(a[3],Sum))

# 예제.5
# lst = [10,20,30,40,50]
# print(lst)
# print(lst[1:3])
# print(lst[2:4])
# print(lst[3:])
# print(lst[:2])
# print(lst[-5:-2])

# ["List" 복사]

# : 얇은 복사 , 깊은 복사 2가지 종류의 복사가 있다.
# : 얇은 복사는 [원본 List]의 주소 값을 [사본 List]에 적용하는 형태의 복사
# : ( 즉, 주소 값만 복사하는 형태를 말한다. )
# : 얇은 복사는 쉽게, 기존의 List에 또 다른 이름이 부여되는 것이다.

# [EX] : 얇은 복사 (바로가기 만들기)
# lst1 = [1,2,3,4,5]
# lst2 = lst1

# # 예제.6 : 얇은 복사
# lst1=[1,2,3,4,5]
# lst2=lst1
# lst2[0] = 100
# print("lst1[0] : ",lst1[0])
# print("lst2[0] : ",lst2[0])
# print(id(lst1), id(lst2)) #id함수는 주소값을 출력 할 수 있다.
# # 얇은 복사시 두 리스트의 주소는 똑같게 된다.


# : 깊은 복사는 [원본 List]의 주소 값을 복사하는 것이 아닌 새로운 [사본 List]를 생성하여 데이터를 복사한다.
# : 일반적으로 우리가 사용하는 형식의 복사라고 생각한다.
# : 단, Import를 이용하여 copy 기능을 불러와서 사용해야 한다.

#[EX] : 깊은 복사
# import copy
# lst1=[1,2,3,4,5]
# lst2=copy.copy(lst1)
# lst2[0] = 100
# print("lst1[0] : ",lst1[0])
# print("lst2[0] : ",lst2[0])
# print(id(lst1), id(lst2)) #id함수는 주소값을 출력 할 수 있다.
# 깊은 복사시 두 리스트의 주소는 같지 않게 된다.