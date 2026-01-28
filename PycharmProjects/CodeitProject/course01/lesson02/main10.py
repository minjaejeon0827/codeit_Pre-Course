# 10. 세 수의 곱
# 실습 설명
# 세 수의 곱을 알려주는 프로그램을 만들려고 합니다.
#
# 파라미터로 정수 값 세 개를 받고, 세 수의 곱을 출력하는 함수 multiply_three_numbers를 만들어 보세요.
#
# 실습 결과
# 105
# 756
# -126

# 힌트 1 - 파이썬에서 곱셈은 * 기호를 사용해서 표현할 수 있습니다.
#         예를 들어서 2 곱하기 4는 2 * 4.
# 힌트 2 - 파이썬에서 세 수 이상의 곱셈도 다음과 같이 표현할 수 있습니다.
#         예를 들어서 3 곱하기 4 곱하기 2는 3 * 4 * 2.
# 힌트 3 - 파이썬에서 함수의 파라미터는 함수의 괄호 안에 넣어 주면 됩니다.
#         def multiply_three_numbers(여기에_파라미터가_들어갑니다):
# 힌트 4 - 파이썬에서 여러 개의 파라미터를 전달하기 위해서는 쉼표(,)를 활용하면 됩니다.
#         def multiply_three_numbers(num_1, num_2, num_3):

# 함수 매개변수와 인수
# 참고 URL - https://wikidocs.net/24#_4
# 참고 2 URL - https://www.codeit.kr/community/threads/10416
# 참고 3 URL - https://www.codeit.kr/community/threads/5998
# 참고 4 URL - https://mingrammer.com/understanding-the-asterisk-of-python/

# math.prod 함수 - 이터러블(iterable) 객체(튜플, 리스트 등등...)에 속한 모든 요소 곱하기
# 참고 URL - https://docs.python.org/ko/3/library/math.html#math.prod

# 코드를 작성하세요.
import math   # math 모듈 import

def multiply_three_numbers(*numbers):
    """
    Description: [테스트] 튜플(또는 리스트)에 저장된 여러가지 수(*numbers)의 곱셈 값 출력

    Parameters: *numbers - 실수값 저장된 튜플 객체 (가변인수)

    Returns: None
    """

    # print(*numbers)
    # 주의사항 - 가변인자의 값(numbers)을 직접 사용(sum, math.prod 함수 인자 전달 등등...)할 때는 *를 빼고 사용
    # print(numbers)   # 튜플(또는 리스트) 객체 출력
    # print(sum(numbers))
    print(math.prod(numbers))

# def multiply_three_numbers(numA, numB, numC):
#     """
#     Description: [테스트] 세 가지 수(numA, numB, numC)의 곱 출력
#
#     Parameters: numA - 실수값 저장된 변수
#                 numB - 실수값 저장된 변수
#                 numC - 실수값 저장된 변수
#
#     Returns: None
#     """
#
#     print(numA * numB * numC)

# def multiply_three_numbers(num_1, num_2, num_3):
#     """
#     Description: [테스트] 세 가지 수(num_1, num_2, num_3)의 곱 출력
#
#     Parameters: num_1 - 실수값 저장된 변수
#                 num_2 - 실수값 저장된 변수
#                 num_3 - 실수값 저장된 변수
#
#     Returns: None
#     """
#
#     print(num_1 * num_2 * num_3)


# 테스트 코드
multiply_three_numbers(7, 3, 5)
multiply_three_numbers(21, 4, 9)
multiply_three_numbers(-7, 6, 3)