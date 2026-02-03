# 09. 변수의 scope

# 참고
# scope는 한국말로 '범위'라고 한다.
# 함수 내 선언한 지역 변수(로컬변수 - Local Variable)란?
# 해당 함수 내에서만 사용할 수 있는 변수 의미
# 예를들어 지역 변수(로컬변수 - Local Variable) x의 스코프 즉, 해당 변수 x가 유효한 범위는 변수 x를 선언한 my_function 함수 내부만 해당된다.
# 또한 함수 파라미터도 지역 변수(로컬변수 - Local Variable)이다.

# 글로벌 변수(Global Variable)란?
# 함수 밖에 정의한 변수는 글로벌 변수(Global Variable)라고 부른다.
# 지역 변수(로컬변수 - Local Variable)와 다르게 글로벌 변수(Global Variable)는 모든 곳에서 사용할 수 있다.
# 예를들어 글로벌 변수(Global Variable) x의 스코프 즉, 글로벌 변수(Global Variable) x가 유효한 범위는 해당 변수를 선언한 프로그램 전체에 해당된다.

# 정리
# 모든 변수에는 scope, 즉 변수가 유효한 범위가 있다.
# 가장 대표적으로는 지역 변수(로컬변수 - Local Variable)와 글로벌 변수(Global Variable)로 나눌 수 있다.
# 지역 변수(로컬변수 - Local Variable)는 해당 변수를 정의한 함수 내에서만 사용 가능하다.
# 함수 파라미터 또한 해당 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.
# 반대로 글로벌 변수(Global Variable)는 해당 변수를 정의한 프로그램 전체에서 사용 가능하다.
# 함수에서 어떤 변수를 사용하려고 하면 해당 변수와 같은 이름을 가진 지역 변수(로컬변수 - Local Variable)가 있는지 먼저 찾아서 사용한다.
# 만약 같은 이름을 가진 지역 변수(로컬변수 - Local Variable)가 없으면 같은 이름을 가진 글로벌 변수(Global Variable)가 있는지 찾는다.
# 만약 같은 이름을 가진 지역 변수(로컬변수 - Local Variable)와 글로벌 변수(Global Variable) 둘 다 없으면 아래 예시처럼 오류가 발생한다.
# (예) "NameError: name 'x' is not defined"

x = 2   # x 글로벌 변수(Global Variable) 선언 및 값 할당

def my_function():
    """
    Description: 함수 내 지역 변수(로컬변수 - Local Variable) x 값 출력
                 함수에서 변수 사용시 항상 지역 변수(로컬변수 - Local Variable)가 먼저 있는지 확인하고,
                 만약 없으면 글로벌 변수(Global Variable) 있는지 확인. (지역변수 우선 주의)

    Parameters: 없음.

    Returns: None
    """

    x = 3   # 함수 내 지역 변수(로컬변수 - Local Variable) x 선언 및 값 할당
    print(x)   # 결과값: 3 출력 -> 함수 내 지역 변수(로컬변수 - Local Variable) x에 저장된 값 출력

my_function()
# 아래와 같이 오류 메시지 출력되어 x = 2 글로벌 변수(Global Variable) 선언 및 오류 보완 완료 (2026.02.03 minjae)
# 오류 메시지 - "NameError: name 'x' is not defined"
# 오류 원인 - 'x'라는 이름 가진 변수 선언 안 해서 오류 발생.
print(x)   # 결과값: 2 출력
# 결과값: 2 출력 이유
# x = 2는 글로벌 변수(Global Variable)이다.
# x = 3은 my_function 함수 내에서 정의한 지역 변수(로컬변수 - Local Variable)이다.
# x라는 변수 이름은 같지만 하나는 글로벌 변수(Global Variable) 이고(x = 2),
# 다른 하나는 함수 내 에서만 사용할 수 있는 지역 변수(로컬변수 - Local Variable) 이다.(x = 3)
# 위의 코드 print(x) 실행시 해당 변수 x는 글로벌 변수(Global Variable) (x = 2)에 저장된 값 2가 출력된다.

def global_my_function():
    """
    Description: 글로벌 변수(Global Variable) x 값 출력
                 함수에서 변수 사용시 항상 지역 변수(로컬변수 - Local Variable)가 먼저 있는지 확인하고,
                 만약 없으면 글로벌 변수(Global Variable) 있는지 확인. (지역변수 우선 주의)

    Parameters: 없음.

    Returns: None
    """

    print(x)

global_my_function()
# 아래와 같이 오류 메시지 출력되어 x = 2 글로벌 변수(Global Variable) 선언 및 오류 보완 완료 (2026.02.03 minjae)
# 오류 메시지 - "NameError: name 'x' is not defined"
# 오류 원인 - 'x'라는 이름 가진 변수 선언 안 해서 오류 발생.
print(x)

# 기타
def square(x):
    """
    Description: 정사각형 넓이 값 구하기
                 함수 파라미터 x도 square 함수 내에서만 사용 가능한 지역 변수(로컬변수 - Local Variable)이다.

    Parameters: x - 정사각형 한 변의 길이

    Returns: None
    """
    
    return x * x

print(square(3))