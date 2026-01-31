# 02. 자료형 개요
# 참고
# 컴파일 실행 후 콘솔(Console) 창 출력 메시지 의미
# Process finished with exit code 0
# 직역하면 종료 코드 0으로 프로그램이 종료되었다는 것인데,
# 보통 0 은 에러 없이 프로그램이 성공적으로 실행되었다는 것을 의미함.
# 그래서 위 메시지가 나오면 프로그램이 잘 실행되었다고 생각하면 된다.

# 파이썬 코드 스타일 가이드 라인 (PEP 8 – Style Guide for Python Code)
# 참고 URL - https://www.python.org/dev/peps/pep-0008

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