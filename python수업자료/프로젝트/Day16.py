'''
# 예제.1
Str = "String Indexing"
print(Str[0])
print(Str[3])
print(Str[8])

Str2 ="String Slicing"
print(Str2[:6])
print(Str2[7:])

for val in Str:
    print(val,end="")
print()

Str3 = Str +" "+ Str2
print(Str3)
print(Str3 * 3)

# 예제.2
Str = "python is easy. programming"
print(Str)
print(Str.upper())
print(Str)
Str = Str.lower()
print(Str)
Str = Str.title()
print(Str)
Str = Str.swapcase()
print(Str)
# 예제.3
st="Have a nice day"
print(st)
print(st.count("a"))
print(st.count("day"))
print(st.count("dak"))

#함수를 이용 하지 않을 경우 밑의 반복문을 만들어서 구해야 한다.
cnt_a= 0
for i in st:
    if i=='a':
        cnt_a +=1
print(cnt_a)
#단일 문자의 경우는 위와같이 찾을 수 있지만
#문자열의 경우는 훨씬 어려운 식을 만들어야 한다.
#하지만 파이썬에서는 그냥 함수를 이용하면 되므로 편하다.


# 예제.4
st="Have a nice day"
print(st)
print(st.find("day"))
print(st.find("dak"))
print(st.index("day"))
# print(st.index("dak"))

# 예제.5
st="Have a nice day"
print(st.find('a',2))
print(st.find('a',4))
print(st.find('a',6))
print(st.find('a',14))
# 내풀이
st='Have a nice day Have a nice day Have a nice day'
print("a 개수 : {}".format(st.count("a")))
lst=[]
i=0
for i in range(len(st)-1):
    cnt=st.find('a',i)
    if cnt not in lst:
        lst.append(cnt)
    
print(lst)

# 강사풀이
st='Have a nice day Have a nice day Have a nice day'
cnt = 0
ls = []
for i in st:
    cnt = st.find('a',cnt)
    if cnt !=-1:
        ls.append(cnt)
        cnt+=1
print("a 개수: ",st.count('a'))
print("첨자: ",ls)
#강사풀이 분석해볼것


# 예제.5
st = " 파이썬 "
print("*",st,"*")
print("*",st.strip(),"*")
print("{}{}{}".format("*",st.strip(),"*"))
print(st)
st=st.strip()
print(st)

st="파이썬파"
print(st)
print(st.strip("파"))
print(st.lstrip("파"))
print(st.rstrip("파"))

# 예제.6
st="2020/10/08"
print(st)
print(st.replace('/','.'))
print(st.replace(st[:4],"2021"))
#슬라이싱으로 표현한후 교체시킬 수 도 있다.
st=st.replace('/','.')
print(st)

# 예제.7
st="""Have a nice day
Have a nice day
Have a nice day"""
#이렇게 하면 엔터값도 문자열의 일부로 저장할 수 있다.
print(st)
'''


# quiz.2
st="""김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일"""


# 내풀이
st=st.replace("-",":")
print(st)

cnt = 0
ls = []
for i in st:
    cnt = st.find("20",cnt)
    if cnt !=-1:
        ls.append(cnt)
        cnt+=1
print("20의 개수: ",st.count("20"))
print("첨자: ",ls)

for i in range(len(ls)):
    st=st.replace(st[ls[i]:ls[i]+4],"1999")
print(st)

# 강사풀이
st = st.replace('-',":")
i=0
for k in range(st.count(":")):
    i = st.find(":",i+1)
    st = st.replace(st[i+1:i+5],"1999")