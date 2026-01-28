# 11. return문
# 변수: 값을 저장하는 역할
# 함수: 명령을 저장하는 역할
# 파라미터: 함수에 넘거주는 (인자)값
# return문: 함수에게 뭔가 정보를 주면 어떤 다른 정보를 돌려준다.

# 함수 매개변수와 인수
# 참고 URL - https://wikidocs.net/24#_4
# 참고 2 URL - https://www.codeit.kr/community/threads/10416
# 참고 3 URL - https://www.codeit.kr/community/threads/5998
# 참고 4 URL - https://mingrammer.com/understanding-the-asterisk-of-python/

# math.prod 함수 - 이터러블(iterable) 객체(튜플, 리스트 등등...)에 속한 모든 요소 곱하기
# 참고 URL - https://docs.python.org/ko/3/library/math.html#math.prod

def get_square(x):
    """
    Description: 정사각형 넓이 값 출력

    Parameters: x - 정사각형 한 변의 길이

    Returns: x * x - 정사각형 넓이 값
    """

    return x * x

print(get_square(3))
# y = get_square(3)   # 지정 연산자(=)
# print(y)

print(get_square(3) + get_square(4))

def print_sum(x, y):
    """
    Description: 두 수의 합(x, y) 출력하기

    Parameters: x - 실수값 저장된 변수
                y - 실수값 저장된 변수

    Returns: None
    """
    
    print(x + y)

print_sum(3, 4)

def get_sum_something(x, y):
    """
    Description: 두 수의 합(x, y) 가져오기

    Parameters: x - 실수값 저장된 변수
                y - 실수값 저장된 변수

    Returns: x + y - 두 수의 합(x, y)
    """
    
    return x + y

print(get_sum_something(3, 4) + 3)