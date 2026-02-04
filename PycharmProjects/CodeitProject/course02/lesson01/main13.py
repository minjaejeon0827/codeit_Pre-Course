# 프로그래밍 핵심 개념 in Python
# 1. 자료형
# 13. 불린형

# 참고
# 파이썬에서는 참(True)과 거짓(False)을 표현하는 자료형을 불린 (Boolean)이라고 합니다.
# 불린 (Boolean)의 두 값은 True와 False이다.

# = (할당 연산자)와 == (동등 연산자) 차이
# = 는 Assignment 즉 할당연산자이다. 해당 연산자 우측에 있는 값을 해당 연산자 좌측 변수에 넣는것이다.
# == 는 equal 즉 동등 연산자이다. 해당 연산자 기준 좌측데이터와 우측데이터가 같다는 의미를 나타낸다.

# 불린 (Boolean)
print(True)
print(False)

# and 연산 - 명제 x AND 명제 y
# - 두 명제가 모두 참(True)이어야 명제 x AND 명제 y 값은 참(True)이다.
# - 두 명제중 하나라도 거짓(False)이면 명제 x AND 명제 y 값은 거짓(False)이다.
print("and 연산")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or 연산 - 명제 x OR 명제 y
# - 두 명제중 하나라도 참(True)이면 명제 x OR 명제 y 값은 참(True)이다.
# - 두 명제가 모두 거짓(False)이어야 명제 x OR 명제 y 값은 거짓(False)이다.
print("or 연산")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not 연산 - NOT 명제 x
# 기존 명제의 진리값을 반대로 뒤집어 주는 역할이다.
# - 명제가 참(True)이면 거짓(False)으로 만들어준다.
# - 명제가 거짓(False)이면 참(True)으로 만들어준다.
print("not 연산")
print(not True)
print(not False)

# 숫자 비교 연산
print("숫자 비교 연산")
print(2 > 1)
print(2 < 1)
print(3 >= 2)   # 3은 2보다 크거나 또는 같다. 의미 (or 연산 의미 내포)
print(3 <= 3)
print(2 == 2)   # 2는 2와 같다. 의미
print(2 != 2)   # 2는 2와 같지 않다. 의미

# 문자열 비교 연산
print("문자열 비교 연산")
print("Hello" == "Hello")
print("Hello" != "Hello")

# 숫자 + 문자열 비교 연산 응용
print("숫자 + 문자열 비교 연산 응용")
print(2 > 1 and "Hello" == "Hello")   # True and True

# not 연산 응용
print("not 연산 응용")
print(not not True)   # not not True == not False -> 결과값: True
print(not not False)  # not not False == not True -> 결과값: False

# 숫자 + 비교 연산 응용
print("숫자 비교 연산 응용")
print(7 == 7 or (4 < 3 and 12 > 10))   # True or (False and True) -> True or False -> 결과값: False
x = 3
print(x > 4 or not (x < 2 or x == 3))   # False or not (False or True) -> False or not True -> False or False -> 결과값: False