# 02. 함수의 실행 순서

# 참고
# return문 용도
# return은 출력하기 위해 필요한 게 아니라 함수에서 나오는 어떤 결과 값을 받기 위해서 필요하다.

# hello 함수를 정의한다고 해서 hello 함수가 실행되는 건 아니다. 실제로 hello 함수를 호출해야 실행된다.
def hello():
    """
    Description: [테스트] 인삿말 출력

    Parameters: None

    Returns: None
    """
    
    print("Hello!")   # "Hello!" 문자열 출력
    print("Welcome to Codeit!")   # "Welcome to Codeit!" 문자열 출력

print("hello 함수 호출 전")
hello()   # hello 함수 호출(실행)
print("hello 함수 호출 후")

# square 함수를 정의한다고 해서 square 함수가 실행되는 건 아니다. 실제로 square 함수를 호출해야 실행된다.
def square(x):
    """
    Description: 정사각형 넓이 값 출력

    Parameters: x - 정사각형 한 변의 길이

    Returns: x * x - 정사각형 넓이 값
    """

    return x * x

print("square 함수 호출 전")
print(square(3) + square(4))   # (3 * 3) + (4 * 4) -> 결과값: 25
print("square 함수 호출 후")


# 기타
def hello():     #  use no 'return'
    print("hello!")
    print("welcome to codeit!")
    return None     # regard as it is here.
print("before caling fuction")
print(hello())
print("after calling function")

def square(x):
    print("why come it out as None in according to a word 'return'")
    return x * x

print("before")
print(square(3) + square(4))
print("after")
""" excercise upper 2 sentences in the console. """

