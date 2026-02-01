# 06. 형 변환

# 참고
# 형 변환(Type Conversion 또는 Type Casting)을 하면 값을 한 자료형에서 다른 자료형으로 바꿔줄 수 있다.
# (예) 정수형 -> 소수형 / 소수형 -> 정수형 / 소수형 -> 문자열 / 문자열 -> 정수형 등등...

# 소수형 -> 정수형 형변환
print(int(3.8))   # 결과값 - 3

# 정수형 -> 소수형 형변환
print(float(3))   # 결과값 - 3.0

# 문자열 -> 정수형 형변환
print(int("2") + int("5"))   # 결과값 - 7

# "print(int(print(str(3)+str(5)))+23)" 코드 실행시 아래와 같은 오류 발생.
# 오류 메시지 - "TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'"
# 오류 의미 - print()함수 실행시 None 값 반환하는데,  이 None이라는 자료형이 "정수형으로된문자열" 혹은 실수형 값이 아니여서
#            35만 출력되고 더이상 진행이 되지않는 오류 발생
# print(int(print(str(3)+str(5)))+23)   # 결과값 - 35만 출력 되고 오류 발생
print(int(str(3)+str(5))+23)

# 문자열 -> 소수형 형변환
print(float("1.1") + float("2.5"))   # 결과값 - 3.6

# 정수형 -> 문자열 형변환
print(str(2) + str(5))   # 결과값 - "25"

# "print("제 나이는 " + age + "살입니다.")" 코드 실행시 아래와 같은 오류 발생.
# 오류 메시지 - "TypeError: can only concatenate str (not "int") to str"
# 오류 의미 - 문자열(str)과 정수형(int)을 연결시킬 수 없다는 의미
age = 7
# print("제 나이는 " + age + "살입니다.")
print("제 나이는 " + str(age) + "살입니다.")   # 결과값 - 제 나이는 7살입니다.

# "print(int("Hello World!"))" 코드 실행시 아래와 같은 오류 발생.
# 오류 메시지 - "ValueError: invalid literal for int() with base 10: 'Hello World!'"
# 오류 의미 - "Hello World!" 문자열(str)을 정수형(int)으로 바꿀 수 없다는 의미
# print(int("Hello World!"))

# 기타
print("Hello," + "World")  # 출력: Hello,World
print("Hello, " + "World") # 출력: Hello, World
print("I'm" + str(20) + "years old.")   # 출력: I'm20years old.
print("I'm " + str(20) + " years old.") # 출력: I'm 20 years old.
