# 프로그래밍 핵심 개념 in Python
# 2. 추상화
# 12. 스타일

# 참고
# 이해하기 쉬운 코드가 좋은 스타일을 가진 좋은 코드라고 할 수 있다.
# 코드의 스타일은 그냥 내눈에 보기 좋다고 되는게 아니다.
# 함께 작업하게 될 사람들과 맞춰가야 하는 부분이다.
# 예를들어 파이썬 같은 경우에는 가장 많이 사용되는 스타일 가이드인 PEP8이 있다.
# 하여 웬만하면 PEP8에 나온 규칙들을 따라서 개발하는게 좋다.

# 파이썬 코드 스타일 가이드 라인 (PEP 8 – Style Guide for Python Code)
# 참고 URL - https://www.python.org/dev/peps/pep-0008
# 참고 2 URL - https://pep8.org/
# 참고 3 URL - https://peps.python.org/pep-0008/

# 안 좋은 코드 설명
# 문법적으로는 아무런 문제 없고 실행하면 의도한 출력값이 나온다.
# 그럼에도 불구하고 아래 안 좋은 코드 예시와 같은 코드는 절대로 좋은 코드라고 할 수 없다.
# 해당 코드를 읽는 사람 입장에서 생각해보면, 딱 봤을 때 이 프로그램의 목적이 뭔지도 모르겠고
# 숫자들이 뭘 의미하는지 알 수가 없다.
# 가독성이 굉장히 떨어지는 안 좋은 스타일의 코드라고 할 수 있다.
# 아래 코드의 목적은 원의 둘레와 원의 넓이를 계산하는 것이다.
# 그 목적이 잘 드러나려면 코드의 스타일을 개선해야 한다.
# 안 좋은 코드 예시에서 숫자들을 하드코딩 식으로 그냥 썼다면
# 조금 개선된 코드 예시를 보면 숫자를 a, b 변수에 넣어서 사용했다.
# 조금 개선된 코드 예시가 안 좋은 코드 예시 보다 낫긴 하지만,
# a, b 변수가 뭘 의미하는지 모르기 때문에 아직도 이 코드가 뭘 하는지 알기 어렵다.
# 하여 a, b 변수에 주석을 추가했다. (예) # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용) / # 반지름
# 하지만 그래도 a, b 변수 이름을 아무렇게나 지어서 뭘 나타내는 변수인지 알기는 어렵다.
# 그래서 조금더 개선된 코드 예시처럼 변수 이름 수정했다. (예) (기존) a, b -> (변경) pi, radius
# 다만, pi 변수를 값이 절대로 바뀌지 않는 상수(constant)이므로
# 조금 더 개선된 코드 예시 2 처럼 pi 변수 이름을 영어 대문자 PI로 변경한다.
# 여기서 코드의 가독성을 높이기 위해 스페이스키(space)와 엔터키(enter)를 좀 쓰면 아래처럼
# 조금 더 개선된 코드 예시 3 처럼 개선할 수 있다.
# 띄어쓰기나 빈줄(White Space)을 적절히 사용하면 보기 좋은 코드를 만들 수 있다.
# 띄어쓰기나 빈줄(White Space) - 엔터키(enter) - 줄바꿈 / 스페이스키(space) - 연산자(=, *) 앞뒤로 한 칸씩 띄어쓰기
# 또한 여기서 계산 수식을 누구나 이해할 수 있도록 코드를 함수로 구현해서 수정하면
# 개선 완료된 코드 예시 처럼 개선할 수 있다.


# 안 좋은 코드 예시 
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

# 조금 개선된 코드 예시
a=3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)
b=4   # 반지름
print(2*a*b)
print(a*b*b)
b=8   # 반지름
print(2*a*b)
print(a*b*b)

# 조금 더 개선된 코드 예시
pi=3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)
radius=4   # 반지름
print(2*pi*radius)
print(pi*radius*radius)
radius=8   # 반지름
print(2*pi*radius)
print(pi*radius*radius)

# 조금 더 개선된 코드 예시 2
# 상수(constant) PI
PI=3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)
radius=4   # 반지름
print(2*PI*radius)
print(PI*radius*radius)
radius=8   # 반지름
print(2*PI*radius)
print(pi*radius*radius)

# 조금 더 개선된 코드 예시 3
# 상수(constant) PI
PI=3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)

radius=4   # 반지름
print(2*PI*radius)
print(PI*radius*radius)

radius=8   # 반지름
print(2*PI*radius)
print(pi*radius*radius)

# 개선 완료된 코드 예시
# 상수(constant) PI
PI = 3.14   # 원주율 '파이' (용도 - 원의 둘레나 원의 넓이 계산할 때 사용)

def calculate_circumference(r):
    """
    Description: 원의 반지름을 받아서 원의 둘레 계산
                 함수 파라미터 r도 calculate_area 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.

    Parameters: r - 원의 반지름 길이

    Returns: 2 * PI * r - 원의 둘레
    """
    
    return 2 * PI * r

def calculate_area(r):
    """
    Description: 원의 반지름을 받아서 원의 넓이 계산
                 함수 파라미터 r도 calculate_area 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.

    Parameters: r - 원의 반지름 길이

    Returns: PI * r * r - 원의 넓이
    """

    return PI * r * r

radius = 4   # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8   # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))