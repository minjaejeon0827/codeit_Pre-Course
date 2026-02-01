# 06. 함수

# 엔터키(Enter Key) - 가독성 향상 용도
# 참고 - 엔터키(Enter Key)를 포함하여 발생하는 공백도 메모리를 차지하기 때문에 관계는 있지만, 
#       현재 컴퓨터 메모리를 생각한다면 무시해도 된다.
# 참고 URL - https://www.python.org/dev/peps/pep-0008/#blank-lines

# 변수는 값을 저장하고 함수는 명령을 저장하는 역할이다.
# 함수 예시 - print()
# 참고사항 - 개발자는 print() 함수가 내부적으로 어떻게 동작하는지 자세히는 모른다.
# 다만, 이런 내부적인 걸 몰라도 아무 문제 없이 사용할 수 있다는 게 추상화(Abstraction)의 장점이자 목적이다.
# 내부적으로 동작하는 명령의 복잡한 디테일을 다 알 필요 없이 주요 기능에만 집중하기 위해 함수를 사용함.
# print() 함수처럼 프로그래밍 언어를 만든 개발자들이 미리 구현해서 사용자들에게 기본 제공하는 함수를 '내장 함수'라고 부른다.
# 내장 함수가 아니라 사용자들이 직접 정의해서 구현하는 함수의 예시는 아래 hello 함수와 같다.

# semicolon(;) 은 어떤 명령문을 다른 명령문과 구분하기 위해 쓰게 된다.
# ;는 파이썬에서도 사용해도 되고 생략해서 사용해도 된다.
# ;는 코드의 맺음 역할을 한다.

def hello():   # def 기호 사용하여 구현한 함수 정의의 첫줄을 함수의 '헤더'라고 부른다.
    """
    Description: [테스트] 사용자 정의 함수

    Parameters: None

    Returns: None
    """

    # 해당 hello 함수는 아래 2 줄의 명령 저장 및 실행
    print("Hello!")
    print("Welcome to Codeit!")

# hello 함수 3번 호출
hello()
hello()
hello()

# 사용자 정의 함수 예시
def sum(a, b):
    return a+b

print(sum(3,4))

def hello_str():
    return "Hello"

print(hello_str() * 2)

# 사용자 정의 함수 예시
# 참고 URL - https://www.programiz.com/python-programming/function

# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)
#
# Parameters (arguments) through which we pass values to a function. They are optional.
#
# Example of a function
# def greet(name):
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("Hello, " + name + ". Good morning!")
