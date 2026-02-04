# 프로그래밍 핵심 개념 in Python
# 1. 자료형
# 02. 숫자형 심화

# 참고
# 파이썬 부동소수점 (decimal 모듈)
# 참고 URL - https://docs.python.org/ko/3.9/tutorial/floatingpoint.html
# 참고 2 URL - https://docs.python.org/ko/3/tutorial/floatingpoint.html
# 참고 3 URL - https://blog.winterjung.dev/2020/01/06/floating-point-in-python
# 참고 4 URL - https://realpython.com/python-rounding/#the-decimal-class
# import decimal
# from decimal import Decimal

# round (반올림)
# 참고 URL - https://realpython.com/python-rounding/#rounding-half-to-even

# floor division (버림 나눗셈 - 몫 연산)
# 정수형 // 정수형 = 정수형
# 소수형 // 정수형 = 소수형
# 정수형 // 소수형 = 소수형
# 소수형 // 소수형 = 소수형
print(7 // 2)
print(8 // 3)
print(8.0 // 3)

# round (반올림)
# round 함수로 전달한 인자값을 정수로 반올림
print(round(3.1415926535))   # 정수 반올림
print(round(3.1415926535, 2))   # 소수점 둘째 자리 소수 반올림
print(round(3.1415926535, 4))   # 소수점 넷째 자리 소수 반올림
print(round(0.125, 2))   # 결과값: 0.13
print(round(0.135, 2))   # 결과값: 0.14

import decimal
print(decimal.getcontext())   # 반올림 모드 확인
ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_HALF_UP   # 반올림 모드 변경
print(decimal.getcontext())

from decimal import Decimal
print(Decimal("3.141592").quantize(Decimal("1.0000")))   # 반올림(ROUND_HALF_UP모드)
print(Decimal("0.135").quantize(Decimal("1.00")))   # 반올림: 올려서 0.14(UP)
print(Decimal("0.125").quantize(Decimal("1.00")))   # 반올림: 올려서 0.13(UP)