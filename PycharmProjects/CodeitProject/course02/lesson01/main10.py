# 10. 문자열을 포매팅하는 다양한 방식

# 참고
# format 함수
# Syntax : { } .format(value)
# Parameters : (value) : Can be an integer, floating point numeric constant, string, characters or even variables.
# Return type : Returns a formatted string with the value passed as parameter in the placeholder position.
# 참고 URL - https://docs.python.org/ko/3/library/stdtypes.html#str.format

# print 함수 스타일 문자열 포매팅
# 참고 URL - https://docs.python.org/ko/3/library/stdtypes.html#printf-style-string-formatting

# 우리는 앞서 format() 메소드를 이용한 문자열 포매팅 방법을 배웠습니다.
# 하지만 파이썬에는 문자열을 포매팅하는 방법이 몇 가지 더 있는데요.
# 각각 간단하게 소개해 드리겠습니다.

# % 기호
name = "최지웅"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))   # 결과값 - 제 이름은 최지웅이고 32살입니다.
# 이제는 잘 쓰지 않는 오래된 방식입니다.
# %s, %d와 같은 '포맷 스트링'이라는 것을 사용하는데요.
# C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열을 포매팅합니다.

# format() 메소드
name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))   # 결과값 - 제 이름은 최지웅이고 32살입니다.
# 앞에서 배워봤던 방식입니다.

# f-string
name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")
# 제 이름은 최지웅이고 32살입니다.
# 파이썬 3.6에서 추가된 문법인데요.
# 훨씬 편리하기 때문에 최근에 많이 사용하는 방식입니다.

# 기타
num1 = 1
num2 = 3
num3 = num1 / num2

division_d = "{} 나누기 {}은 {}입니다."

print(division_d.format(num1,num2, num3))

division = f"{num1} 나누기 {num2}은 {num3}입니다."
print(division)

x = 10
y = 5

# 기존의 문자열 포맷팅 방식
result = "{} + {} = {}".format(x, y, x + y)
print(result)

# F-string 사용
result_f = f"{x} + {y} = {x + y}"
print(result_f)