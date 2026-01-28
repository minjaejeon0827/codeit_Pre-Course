# 09. 여러 개의 파라미터
# 함수 매개변수와 인수
# 참고 URL - https://wikidocs.net/24#_4
# 참고 2 URL - https://www.codeit.kr/community/threads/10416
# 참고 3 URL - https://www.codeit.kr/community/threads/5998
# 참고 4 URL - https://mingrammer.com/understanding-the-asterisk-of-python/

def hello(name):   # def 기호 사용하여 구현한 함수 정의의 첫줄을 함수의 '헤더'라고 부른다.
    """
    Description: [테스트] 사용자 정의 함수 hello

    Parameters: name - 이름

    Returns: None
    """

    print("Hello!")
    print(name)
    print("Welcome to Codeit!")

hello("Michael")

def print_sum(a, b):
    """
    Description: [테스트] 두 수(a, b)의 합 출력

    Parameters: a - 실수값 저장된 변수
                b - 실수값 저장된 변수

    Returns: None
    """
    
    print(a + b)

print_sum(7, 3)


def print_sum2(num_1, num_2, num_3):
    """
    Description: [테스트] 세가지 수(a, b, c)의 합 출력

    Parameters: num_1 - 실수값 저장된 변수
                num_2 - 실수값 저장된 변수
                num_3 - 실수값 저장된 변수

    Returns: None
    """

    print(num_1 + num_2 + num_3)

print_sum2(7 ,3 ,2)

def print_sum3(*numbers):
    """
    Description: [테스트] 튜플(또는 리스트)에 저장된 여러가지 수(*numbers)의 합 출력

    Parameters: *numbers - 실수값 저장된 튜플 객체 (가변인수)

    Returns: None
    """

    print(*numbers)
    # 주의사항 - 가변인자의 값(numbers)을 직접 사용(sum 함수 인자 전달 등등...)할 때는 *를 빼고 사용
    print(numbers)   # 튜플(또는 리스트) 객체 출력
    print(sum(numbers))

print_sum3(1, 2, 3, 4, 5, 6)

def print_sum4(a = 0, b = 0, c = 0):
    """
    Description: [테스트] 세가지 수(a, b, c)의 합 출력

    Parameters: a - 실수값 저장된 변수  (초기값 0 설정)
                b - 실수값 저장된 변수  (초기값 0 설정)
                c - 실수값 저장된 변수  (초기값 0 설정)

    Returns: None
    """

    print(a + b + c)

print_sum4(7,3,2)   # 12
print_sum4(7,3)     # 10
print_sum4(7)       # 7
print_sum4()        # 0


def function(a, b):
    """
    Description: [테스트] 두 수(a, b, c) 출력 및 곱셈, 비트 연산값 출력

    Parameters: a - 실수값 저장된 변수
                b - 실수값 저장된 변수

    Returns: None
    """
    
    print(a)
    print(b)
    print(a * b)
    # ^ - XOR 비트 연산자 (비트 값이 서로 다른 경우에 1을 반환, 그렇지 않은 경우 0을 반환)
    # 예) (기존) a = 14, b = 21 -> (비트 변환) a = 01110(2), b = 10101(2)
    #     (XOR 연산) a = 01110(2) ^ b = 10101(2) = 11011(2) = 십진수 27
    print(a ^ b)
    # ** - 거듭제곱 연산자
    print(a ** b)

function(14, 21)