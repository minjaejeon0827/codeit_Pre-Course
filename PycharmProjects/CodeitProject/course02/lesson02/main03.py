# 프로그래밍 핵심 개념 in Python
# 2. 추상화
# 03. return문 제대로 이해하기

# 참고
# return문의 역할
# 1. 함수 실행 후 어떤 결과값 돌려주기
# 2. 함수 즉시 종료하기

# 함수에서는 아무것도 return 하지 않았을 때 기본적으로 None이라는 값이 return 되도록 되어 있다.

def square(x):
    """
    Description: 정사각형 넓이 값 구하기

    Parameters: x - 정사각형 한 변의 길이

    Returns: x * x - 정사각형 넓이 값
    """

    print("함수 시작")   # "함수 시작" 문자열 출력
    return x * x   # 3 * 3 리턴(돌려주기) + 함수 즉시 종료하기
    # print("함수 끝")   # 의미 없는 코드(Dead Code) - 바로 위의 줄에 있는 return문(return x * x) 실행시 함수 즉시 종료시키기 때문에 "함수 끝" 문자열 출력 불가

print(square(3))
print("Hello World")