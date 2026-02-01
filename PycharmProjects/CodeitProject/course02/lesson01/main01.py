# 01. 숫자형
# 연산자(+, -, *, %, ** 등등...)
# 정수형  정수형 = 정수형
# 소수형  소수형 = 소수형
# 정수형  소수형 = 소수형

# 참고
# 파이썬 부동소수점 (decimal 모듈)
# 참고 URL - https://docs.python.org/ko/3.9/tutorial/floatingpoint.html
# 참고 2 URL - https://docs.python.org/ko/3/tutorial/floatingpoint.html
# 참고 3 URL - https://blog.winterjung.dev/2020/01/06/floating-point-in-python
# 참고 4 URL - https://realpython.com/python-rounding/#the-decimal-class
# from decimal import Decimal
import decimal

# 덧셈
# print(4 + 7)
# print(4.0 + 7.0)
print(4 + 7.0)

# 뺄셈
# print(2 - 4)
# print(2.0 - 4.0)
print(2.0 - 4)

# 곱셈
# print(5 * 3)
# print(5.0 * 3.0)
print(5.0 * 3)

# 나머지
# print(7 % 3)
# print(7.0 % 3.0)
print(7 % 3.0)

# 거듭제곱
# print(2 ** 3)
# print(2.0 ** 3.0)
print(2.0 ** 3)

# 나눗셈 (/)
# 정수형 / 정수형 = 소수형
# 소수형 / 정수형 = 소수형
# 정수형 / 소수형 = 소수형
# 소수형 / 소수형 = 소수형
print(7 / 2)
print(6 / 2)
print(7.0 / 2)
print(6.0 / 2.0)
print(1.2 / 3.0)   #또는
print(1.2 / 3)   #역시
# 결과값:0.39999999999999997
print(decimal.Decimal('1.2') / decimal.Decimal('3.0'))
print(decimal.Decimal('1.2') / 3)
# 결과값:0.4

# floor division (//) (버림 나눗셈 - 몫 연산)
# 정수형 // 정수형 = 정수형
# 소수형 // 정수형 = 소수형
# 정수형 // 소수형 = 소수형
# 소수형 // 소수형 = 소수형
print(7 // 2)
print(6 // 2)
print(7.0 // 2)
print(6.0 // 2.0)

# 다중 사칙 연산
# 덧셈/뺄셈 보다 곱셈/나눗셈이 먼저 계산
print(2 + 3 * 2)
print(2 * (2 + 3))