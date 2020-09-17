'''
# [예제.1]
import turtle
turtle.forward(100)
turtle.mainloop()

#[문제.1]
import turtle
val = int(input("한변의 길이입력: "))
turtle.forward(val)
turtle.left(120)
turtle.forward(val)
turtle.left(120)
turtle.forward(val)
turtle.mainloop()

#[문제.2]
import turtle
v1 = int(input("가로길이 입력: "))
v2 = int(input("세로길이 입력: "))
turtle.forward(v1)
turtle.left(90)
turtle.forward(v2)
turtle.left(90)
turtle.forward(v1)
turtle.left(90)
turtle.forward(v2)
turtle.mainloop()

#[문제.3]
import turtle
val = int(input("한변의 길이입력: "))
turtle.forward(val)
turtle.left(360/6)
turtle.forward(val)
turtle.left(360/6)
turtle.forward(val)
turtle.left(360/6)
turtle.forward(val)
turtle.left(360/6)
turtle.forward(val)
turtle.left(360/6)
turtle.forward(val)
turtle.mainloop()

# [예제.2]
A = 3
B = 2
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A//B)
print(A%B)
print(A**B)

# [예제.3]
A = 3
B = 2
print(A == B)
print(A != B)
print(A > B)
print(A < B)
print(A >= B)
print(A <= B)

# [예제.4]
print(0 and 0," : ",False and False)
print(1 and 0," : ",True and False)
print(0 and 1," : ",False and True)
print(1 and 1," : ",True and True)
print("not : ",not 0," : ",not False)
print("not : ",not 1," : ",not True)
print(0 or 0," : ",False or False)
print(1 or 0," : ",True or False)
print(0 or 1," : ",False or True)
print(1 or 1," : ",True or True)
print("not : ",not(0 or 0)," : ",not(False or False))
print("not : ",not(1 or 1)," : ",not(True or True))

# [예제.5]
print(1 in (1,2,3))
print(1 not in (1,2,3))
print(4 in (1,2,3))
print(4 not in (1,2,3))

# [예제.6]
num1 = 1
num2 = "1"
print(type(num1) is type(num2))
print(type(num1) is not type(num2))
'''


