# 프로그래밍 핵심 개념 in Python
# 1. 자료형
# 14. type 함수

# 참고
# 파이썬으로 코딩 하다 보면 쓰고 있는 값이 어떤 자료형인지 확실하지 않을 때가 있다.
# 그럴 때 type이라는 함수를 써주면 어떤 자료형인지 확인할 수 있다.

print(type(type(3)))   # 자료형 - type (자료형 클래스들의 type 이라는 부모 class 있음.)

print(type(3))   # 자료형 - int(정수형)
print(type(3.0))   # 자료형 - float(소수형 - floating point 줄임말)
print(type("3"))   # 자료형 - str(문자열 - string 줄임말)

print(type("True"))   # 자료형 - str(문자열 - string 줄임말)
print(type(True))   # 자료형 - bool(불린 - Boolean 줄임말)

def hello():
    """
    Description: [테스트] 인삿말 출력

    Parameters: None

    Returns: None
    """

    print("Hello world!")

print(type(hello))   # 자료형 - function(함수형 - 사용자 정의 함수 의미. 함수 또한 하나의 자료형이다.)
print(type(print))   # 자료형 - builtin_function_or_method(내장되어 있는 함수형 의미. 사용자가 정의한 함수가 아니라 파이썬에 기본적으로 내장되어 있는 함수이다. 함수 또한 하나의 자료형이다.)

# 기타
print(type(print(3 > 1)))   # 자료형 - NoneType(값이 비어있음 - print(3 > 1) 실행후 반환되는 값은 None이다.)

# 아래 구현한 코드의 경우 type(number) 함수 보다는 isinstance(number, int) 함수 사용해서
# 특정 자료형(int)의 객체인지 확인하는 방식으로 실무 프로젝트에서 아래와 같이 구현한다.
# number = 3
# print('숫자니?')
# if type(number) == int:
#     print("그렇네")
# else:
#     print("아닌데?")

number = 3
print('숫자니?')
if isinstance(number, int):
    print("그렇네")
else:
    print("아닌데?")