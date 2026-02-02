# 04. return과 print의 차이

# 참고
# return문 vs print문 차이
# 참고 URL - https://www.codeit.kr/community/questions/UXVlc3Rpb246NWUzNDUyMjU4MGU1MTMzNzNkOTYyZTk5
# 참고 2 URL -


def print_square(x):
    """
    Description: 정사각형 넓이 값 출력

    Parameters: x - 정사각형 한 변의 길이

    Returns: None
    """

    print(x * x)

def get_square(x):
    """
    Description: 정사각형 넓이 값 구하기

    Parameters: x - 정사각형 한 변의 길이

    Returns: x * x - 정사각형 넓이 값
    """

    return x * x

print_square(3)
get_square(3)   # 결과값 - 9 리턴 되지만 해당 값이 출력되지 않음.
print(get_square(3))
print(print_square(3))   # 결과값 - None / print_square 함수 호출시 return문이 따로 없으므로 None 리턴되서 print 함수 호출시 결과값 - None 출력 (print(None) 에 의해 None 이 출력된다.)

# None 이 반환되는 경우는 두가지이다.
# 1. return 이 명시되지 않았거나
# 2. return 이 실행될 수 없거나

def print_number():
    """
    Description: 숫자 출력

    Parameters: 없음.

    Returns: None
    """

    print(3)
    # return None이 생략되어 있다고 내부적으로 처리

print_number()    # 1 - 1번에서는 print(3) 에 의해 3 이 화면에 출력된다. 그리고 return 이 없으니 return None 에 의해 None 이 반환되지만 None 이 화면에 출력되진 않는다.
print()    # 줄바꿈
print(print_number())    # 2 - 2번 같은 경우엔 print_number()를 호출하면 먼저 3을 출력하고 그 다음에 None 을 반환한다. 함수 호출한 자리에 None 을 반환하게되니 print(print_number())는 print(None) 이 되고 이에 의해 None 이 화면에 출력된다.

# 추가로 return 이 있더라도 None 이 반환되는 경우도 있을텐데, 아래와 같은 예를 들 수 있다.
# if 조건절(number > 3:) 만족하지 않는 형우 None 반환
def print_number():
    """
    Description: 숫자 출력

    Parameters: 없음.

    Returns: None or '3보다 크다'
    """

    number = 3
    if number > 3:
        return '3보다 크다'

print(print_number())

# 기타
def print_square(x):
    print(x * x)

print_square(3)               # 9가 콘솔에 출력됨. print_square()라는 함수에 파라미터로 3을 넣었을 경우에 답을 프린트 해줌.

print(print_square(3))        # None이 콘솔에 출력됨.
                              # print(type(print_square(3))를 해보면 print_square(3)이 NoneType으로 뜨는걸 확인할수있음.
                              # 따라서 print(None)으로 읽혀 None이 출력됨.

# return 값이 있는 함수
def return_name():
    """
    Description: 문자열 가져오기

    Parameters: 없음.

    Returns: 'peter'
    """
    
    return 'peter'

# return 값이 없는 함수
def print_name():
    """
    Description: 문자열 출력하기

    Parameters: 없음.

    Returns: None
    """
    
    print('peter')    # <<< 실제로는 여기까지 쓰여있습니다
    # return None     <<< 만약 함수에 return 이 정의되어 있지 않다면 파이썬 내부적으로 return None 이 함수 가장 마지막에 쓰여있다고 가정하게 됩니다.

print(return_name())
print_name()

