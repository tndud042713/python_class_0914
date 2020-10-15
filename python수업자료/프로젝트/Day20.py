'''
#파이썬 예외 처리
예외 : 프로그램에서 벌어지는 예외적인 상황을 의미
- 파일을 읽고자 할 때 그 파일이 존재하지 않을 경우
- 어떠한 값을 0으로 나누고자 할 때
- 배열의 인덱스가 범위를 벗어 났을 때
- 사용자의 요구대로 진행이 안될 때
실제로 프로그램을 만들면 무조건 해줘야 되는 것
(예시)
# 10/0 -> 에러
# [],() 리스트나 튜플로 작업할때
# [3] 인데 3번 인덱스보다 큰 수를 사용하면 범위가 넘어간다 ->에러

#기본형식 : try ~ except
try:
    "실제 수행 내용"
except:
    "예외 상황 발생 시 실행 될 내용"


# 발생 Error 지정 -if, elif식과 동일하다.
try:
    "실제 수행 내용"
except SyntaxError:
    "문법적인 오류가 발생 했을때 수행할 내용 작성"
except TypeError:
    "지정 된 형식에 맞지 않는 데이터 입력시 발생"
except:
    "나머지 오류"

#자주 만나는 에러메시지의 종류
FileNotFoundError: 소스코드에서 지정 한 대상 파일이 존재하지 않을 경우 발생
ZeroDivisionError: 특정 숫자 값을 "0"으로 나누었을 때 발생
IndexError:특정 자료형에서 사용중인 인덱스 범위를 벗어났을 경우 발생
SyntaxError:구문 오류, 문법 사용이 잘못 되었을 때 발생
EOFError:파일의 끝일 경우 즉, 더 이상 읽어 들일 내용이 없는 경우에 발생
KeyboardInterrupt: 입력이 취소되었을 경우 발생("Ctrl + C")
'''

'''
# 예제.1
# 예외처리가 없을때 예외를 없애는 방식
num1 = int(input("첫 번째 정수입력: "))
num2 = int(input("두 번째 정수입력: "))
if num2==0:
    print("0으로 나눌 수 없습니다.")
else:
    Div = num1/num2
    print("결과:",Div)

#if문으로 예외를 없애는 것은 한계가 분명히 존재한다.
# 예제.1
while True:
    try: 
        num1 = int(input("첫 번째 정수입력: "))
        num2 = int(input("두 번째 정수입력: "))
        Div = num1/num2
        print("결과:",Div)
        break
    except:
        print("Error 발생 입력값을 확인해 주세요!")
        continue

# 예제.2
while True:
    try: 
        num1 = int(input("첫 번째 정수입력: "))
        num2 = int(input("두 번째 정수입력: "))
        Div = num1/num2
        print("결과:",Div)
        break
    except ZeroDivisionError:
        print("ZeroDivisionError (0 으로 나눌 수 없습니다.)")
    except ValueError:
        print("Value Error! (반드시 정수값을 입력해주세요.)")
    except:
        print("그 외 나머지 Error 발생 시 실행!")

#예제.3
try:
    num = int(input("수 입력: "))
except ValueError:
    print("잘못 된 입력입니다.!")
except:
    print("예외상황 발생")
else: 
    print("예외상황이 발생하지 않았을 경우 실행")
finally:
    print("무조건 실행") # 예외의 유뮤와 상관없이 무조건 실행
'''
'''
# 퀴즈.1
- 인증 프로그램 제작
- 90년생 부터는 "가입불가"
- 90년생 미만은 "가입가능"
- A,ㅁ,ㅋ,구십년,... 이러한 값 입력시 "잘못입력, 숫자를 입력하세요" 문구 출력
'''
'''
try:
    raise Exception("강제 에러 발생!")
except Exception as a:
    print(a)
'''
'''
try:
    idnumber=int(input("인증프로그램 시작(주민번호 앞 6자리를 입력하시오): "))
    a=idnumber//10000
    if a<90 :
        raise Exception("가입가능")
    else:
        raise Exception("가입불가")
except Exception as a:
    print(a)


#강사풀이
try:
    min=input("주민번호 6자리 입력(EX:881020): ")
    if min[0] > '9': #문자열 데이터이므로 인덱싱 구조를 사용할 수 있다.
        raise Exception("잘못입력, 숫자를 입력하세요")
    elif min[0]>'8':
        raise Exception("가입불가")
except Exception as test:
    print(test)
else:
    print(min,": 가입가능")
finally:
    print("프로그램을 종료합니다.")
'''


'''
# 파일 입출력에서는 경로(path가 매우 중요하다.)
# 예제.1
# 파일 입출력의 기본 형식 "열고 - 쓰고 - 닫기"
f = open("test.txt","w")
str1 = input("내용입력: ")
f.write(str1)
f.close()

# 예제.2
f = open("test.txt","a")
str1 = input("내용입력: ")
f.write(str1)
f.close()


#예제.3
#파일의 내용을 콘솔창에 출력하는 방법
f=open("test.txt", "r")
str1 = f.read()
f.close()
print(str1)
'''

'''
# 참고 #경로를 복사하고 나서 역슬러시(\)에 해당하는 부분은 역슬러시를 한번 더 써줘야 시스템에서 역슬러시로 인식한다.
f = open("D:\\test\\test.txt","w")
str1 = input("내용입력: ")
f.write(str1)
f.close()

f = open("D:\\test\\test.txt","r")
str2 = f.read()
f.close()
print("파일 내부 내용 출력: ",str2)

# 주의할 점: 파일 경로를 입력할때 해당하는 역슬레시는
# 한번 더 입력해줘야 시스템에서 역슬레시로 인식한다.
'''

'''
# 퀴즈
1. 본인의 인적사항을 파일에 저장 후 출력하세요
- 당신의 이름은 : 홍길동
- 홍길동 님의 나이는 : 20살
- 홍길동 님의 주소는 : 산골짜기
- 저장한 파일의 내용을 다른 파일에 그대로 저장도 진행
'''
'''
# 파일출력결과
홍길동
20살
산골짜기


# 내풀이
f = open("D:\\test\\profile.txt","w")
name = input("당신의 이름은: ")
age = input("{}의 나이는: ".format(name))
adr = input("{}의 주소는: ".format(name))
f.write("{}\n".format(name))
f.write("{}\n".format(age))
f.write("{}\n".format(adr))
f.close()

f = open("D:\\test\\profile.txt","r")
str2 = f.read()
f.close()
print(str2)
'''

'''
# 강사 풀이
file = open("info.txt","w")
name = input("당신의 이름은: ")
age = input("{}님의 나이는 : ".format(name))
addr = input("{}님의 주소는 : ".format(name))
file.write(name + "\n" + age + "\n" + addr)
file.close()

file = open("info.txt", "r")
info = file.read()
file.close()
print(info)

file = open("info2.txt","w")
file.write(info)
file.close()
'''
'''
# 예제.4
# 효율적으로 값을 불러오는 코드

file = open("info.txt","r")
while True:
    buf = file.readline()
    if buf =="":
        print("\n더 이상 값이 존재하지 않습니다.")
        file.close()
        break
    print(buf,end="")
'''
'''
file = open("info.txt","r")
buf1 = file.readlines()
print(buf1, type(buf1))

file = open("info.txt","r")
buf2 = file.readlines()
print(buf2, type(buf2))

file = open("info.txt","r")
buf3 = file.readlines()
print(buf3, type(buf3))

file.close()
'''

'''
file = open("info.txt","r")
buf = file.readlines()
for st in buf:
    print(st,end="")
file.close()
'''

