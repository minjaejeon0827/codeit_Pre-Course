# 프로그래밍 핵심 개념 in Python
# 2. 추상화
# 11. 상수

# 참고
# 변수(variable) - 계속해서 값이 바뀌는 변수 (예) radius
# 상수(constant) - 처음에 할당된 값이 바뀌지 않는 변수 (예) PI
# 상수 정의 규칙 - 이름 지을 때 모든 글자를 영어 대문자로 한다.

# 상수 이름 지을 때 영어 대문자로 쓰는 이유?
# 1. 일반 변수와 상수를 쉽게 구분 짓기 위함이다.
# 2. 실수를 하지 않기 위함이다. (물론 상수로 정의한 값을 바꿀 수는 있지만, 상수로 정의했다는 건 어떤 일이 있어도 수정하지 않겠다는 의지를 보여주는 것이다.)

# 상수(constant) PI
PI = 3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)

def calculate_area(r):
    """
    Description: 원의 반지름을 받아서 원의 넓이 계산
                 함수 파라미터 r도 calculate_area 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.

    Parameters: r - 원의 반지름 길이

    Returns: PI * r * r - 원의 넓이
    """

    return PI * r * r

radius = 4   # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))