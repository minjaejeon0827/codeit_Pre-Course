# 14. 짝수? 홀수?

# 참고
# 파이썬 삼항 연산자
# 참고 URL - https://wikidocs.net/20701
# 참고 2 URL - https://wikidocs.net/138185

# 실습 설명
# 어떤 수가 짝수인지 홀수인지 판단하는 is_evenly_divisible() 함수를 작성하세요.
# 이 함수는 number(숫자)를 파라미터로 받습니다.
# 짝수인 경우, 즉 number가 2로 나누어떨어질 경우에는 True를 리턴합니다.
# 홀수인 경우, 즉 number가 2로 나누어떨어지지 않을 경우에는 False를 리턴합니다.
#
# 함수 안에는 print() 함수가 아닌, return문을 사용해야 합니다.
# 참고로 불린 개념을 잘 사용하면, 함수를 단 한 줄로 작성할 수 있습니다.
#
# 실습 결과
# False
# False
# True
# True
# False

# 힌트 1 - 7 % 2 == 0은 False입니다. 8 % 2 == 0은 True입니다.
#         위의 경우에는 정수 7과 정수 8을 예로 들었는데요.
#         이 개념을 파라미터 number에 대해 일반화하면 됩니다.
#         되도록 힌트 2를 보지 않고, 직접 완성하시길 바랍니다.
print(7 % 2 == 0)
print(8 % 2 == 0)

# 힌트 2 - 힌트 1을 일반화하면, number % 2 == 0이 됩니다.
#          이 코드를 쓰면 파라미터 number가 짝수인 경우에는 True가, 홀수인 경우에는 False가 나옵니다.
#          이를 return문과 함께 작성하면 됩니다.

# 실습 해설
#
# 해설
# 불린 자료형에서 배운 내용을 복습해 봅시다.
# 7 % 2 == 0은 False이고, 8 % 2 == 0은 True이죠?
# 이 원리를 파라미터 number에 적용해 볼게요.
#
# number가 짝수인 경우에 number % 2 == 0는 True가 나오고,
# number가 홀수인 경우에 number % 2 == 0은 False가 나오는 거죠.
#
# 그러면 is_evenly_divisible() 함수는 그냥 number % 2 == 0을 리턴하면 되는 것입니다.
#
# 모범 답안
def is_evenly_divisible(number):
    """
    Description: 짝수/홀수 여부 판단
                 함수 파라미터 number도 is_evenly_divisible 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.

    Parameters: number - 짝수/홀수 여부 판단할 수

    Returns: number % 2 == 0 - 짝수(True) / 홀수(False)
    """

    return number % 2 == 0


# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

# 코드
def is_evenly_divisible(number):
    """
    Description: 짝수/홀수 여부 판단
                 함수 파라미터 number도 is_evenly_divisible 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.
                 
                 파이썬 삼항 연산자
                 참고 URL - https://wikidocs.net/20701
                 참고 2 URL - https://wikidocs.net/138185

    Parameters: number - 짝수/홀수 여부 판단할 수

    Returns: number % 2 == 0 - 짝수(True) / 홀수(False)
    """

    # 여기에 코드를 작성하세요
    # return (True if number % 2 == 0 else False)   # 파이썬 삼항 연산자 사용 예시
    return number % 2 == 0


# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))