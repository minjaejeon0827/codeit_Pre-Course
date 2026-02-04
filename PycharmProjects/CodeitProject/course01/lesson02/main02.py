# 프로그래밍 시작하기 in Python
# 2. 프로그래밍 기본 개념
# 02. 자료형 개요

# 2와 2.0 사이의 값 비교를 하기 위해 정수 2 -> 실수 2.0 으로 변환 후 값 비교 처리
print(2 != 2.0) # 정수형(Integer)과 소수형(Floating Point) 값 비교

# 데이터 타입(Data Type) 비교 하기 위해 type() 사용.
# 참고 URL - https://chatgpt.com/c/6977176a-5f98-8321-ba5e-03864328ddbd
print(type(2) != type(2.0))   # 정수형(Integer)과 소수형(Floating Point) 데이터 타입 비교
print("Hello" + "World")   # 문자열 덧셈 연산(+)
print((2 != 2.0) and (2 != "2"))   # 정수형(Integer), 소수형(Floating Point), 문자열(String) 값 비교
print((type(2) != type(2.0)) and (type(2) != type("2")))   # 정수형(Integer), 소수형(Floating Point), 문자열(String) 데이터 타입 비교
print(7 > 3)   # 불린(Boolean) 결과값 참(True)
print(7 < 3)   # 불린(Boolean) 결과값 거짓(False)