'''
[ Python 예외 처리 ]
예외 : 프로그램에서 벌어지는 예외적인 상황을 의미
- 파일을 읽고자 할 때 그 파일이 존재하지 않을 경우
- 어떠한 값을 0으로 나누고자 할때  
- 배열의 인덱스를 범위를 벗어 났을때
- 사용자의 요구대로 진행이 안 될때 

# [기본 형식] : try ~ except
try:
    "실제 수행 내용"
except:
    "예외 상황 발생 시 실행 될 내용"

# [발생 Error 지정] 
try:
    "실제 수행 내용"
except SyntaxError:
    "문법적인 오류가 발생 했을때 수행할 내용 작성"
except:
    "나머지 오류"

FileNotFoundError : 소스코드에서 지정 한 대상 파일이 존재하지 않을 경우 발생
ZeroDivisionError : 특정 숫자 값을 "0"으로 나누었을 때 발생
IndexError : 특정 자료형에서 사용중 인 인덱스 범위를 벗어 낫을경우 발생
SyntaxError : 구문 오류, 문법 사용이 잘 못 되었을 때 발생
EOFError : 파일의 끝일 경우 즉, 더 이상 읽어 들일 내용이 없는 경우 발생
KeyboardInterrupt : 입력이 취소되었을 경우 발생 ( "Ctrl + C" )

# [예제.1]
while True:
    try:
        num1 = int(input("첫 번째 정수입력: "))
        num2 = int(input("두 번째 정수입력: "))
        Div = num1 / num2
        print("결과:",Div)
        break

    except:
        print("Error 발생 입력값을 확인해 주세요!")
        continue

print("다음문장 실행!")
print("다음문장 실행!")
print("다음문장 실행!")
print("다음문장 실행!")

# [예제.2]
while True:
    try:
        num1 = int(input("첫 번째 정수입력: "))
        num2 = int(input("두 번째 정수입력: "))
        Div = num1 / num2
        print("결과:",Div)
        break
    except ZeroDivisionError:
        print("Zero Divsion Error! (0으로 나눌 수 없습니다.)")
        continue
    except ValueError:
        print("Value Error! (반드시 정수값을 입력해주세요.)")
    except:
        print("그 외 나머지 Erro 발생 시 실행!")

# [예제.3]
try:
    num = int(input("수 입력: "))
except ValueError:
    print("잘못 된 입력입니다.!")
except:
    print("예외상황 발생!")
else:
    print("예외상황이 발생하지 않았을 경우 실행")
finally:
    print("무조건 실행!")

# [예제.4]
try:
    a = 1
    if a == 1:
        raise Exception("강제 에러 발생!")

except Exception as a:
    print(a)

[ Quiz.1 ]
- 인증 프로그램 제작 
- 90년생 부터는 "가입불가"
- 90년생 미만은 "가입가능"
- A,ㅁ,ㅋ,구십년,. . . 이러한 값 입력시 "잘못입력, 숫자를 입력하세요" 문구출력

try:
    min=input("주민번호 6자리 입력(EX:881020): ")
    if min[0] > '9':
        raise Exception("잘못입력, 숫자를 입력하세요")
    elif min[0] > '8':
        raise Exception("가입불가")
except Exception as test:
    print(test)
else:
    print(min,": 가입가능")
finally:
    print("프로그램을 종료합니다.")

# [예제.1]
f = open("test.txt","w")
str1 = input("내용입력: ")
f.write(str1)
f.close()

# [예제.2]
f = open("test.txt","a")
str1 = input("내용입력: ")
f.write(str1)
f.close()

# [예제.3]
f = open("test.txt","r")
str1 = f.read()
f.close()
print(str1)

# [ 참고 ]
f = open("E:\\Python_S\\AA\\test.txt","w")
str1 = input("내용입력: ")
f.write(str1)
f.close()

[ Quiz ]
1. 본인의 인적 사항을 파일에 저장 후 출력하세요. ( 이름, 나이, 주소 )
- 당신의 이름은 : 홍길동
- 홍길동 님의 나이는 : 20살
- 홍길동 님의 주소는 : 산골짜기
- 저장한 파일의 내용을 다른 파일에 그대로 저장도 진행

[ 파일 출력 결과 ]
홍길동
20살
산골짜기

file = open("info.txt", "w")
name = input("당신의 이름은: ")
age = input("{}님의 나이는: ".format(name))
addr = input("{}님의 주소는: ".format(name))
file.write(name + "\n" + age + "\n" + addr)
file.close()

file = open("info.txt", "r")
info = file.read()
print(info)
file.close()

file = open("info2.txt", "w")
file.write(info)
file.close()

# [예제.4]
file = open("info.txt","r")
while True:
    buf = file.readline()
    if buf == "":
        print("\n더 이상 값이 존재하지 않습니다.")
        file.close()
        break
    print(buf,end="")

file = open("info.txt","r")
buf1 = file.readlines()
print(buf1, type(buf1))
buf2 = file.readlines()
print(buf2, type(buf2))
buf3 = file.readlines()
print(buf3, type(buf3))
file.close()

file = open("info.txt","r")
buf = file.readlines()
for st in buf:
    print(st,end="")
file.close()
'''



