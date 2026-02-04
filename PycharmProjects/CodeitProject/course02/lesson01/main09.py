# 프로그래밍 핵심 개념 in Python
# 1. 자료형
# 09. format 다루기

# 참고
# format 함수
# Syntax : { } .format(value)
# Parameters : (value) : Can be an integer, floating point numeric constant, string, characters or even variables.
# Return type : Returns a formatted string with the value passed as parameter in the placeholder position.
# 참고 URL - https://docs.python.org/ko/3/library/stdtypes.html#str.format

# print 함수 스타일 문자열 포매팅
# 참고 URL - https://docs.python.org/ko/3/library/stdtypes.html#printf-style-string-formatting

print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))   # 출력 순서 - "박지성", "유재석", "빌 게이츠"
# 문자열 출력 순서 변경
# {0} - "박지성" 문자열 의미
# {1} - "유재석" 문자열 의미
# {2} - "빌 게이츠" 문자열 의미
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))   # 출력 순서 - "유재석", "박지성", "빌 게이츠"

num_1 = 1
num_2 = 3
# {0} - 1 정수형 의미
# {1} - 3 정수형 의미
# {2} - 0.3333333333333333 소수형 의미
# (f: 소수형 의미하는 floating point 약자)
# {2:.0f} - 0 소수형 숫자에서 정수 값만 추출 의미 (.0f: 소수형 숫자에서 정수값만 추출)
# {2:.2f} - 0.33 소수점 둘째 자리로 반올림 소수형 의미 (.2f: 소수점 둘째 자리로 반올림 처리)
# {2:.4f} - 0.3333 소수점 넷째 자리로 반올림 소수형 의미 (.4f: 소수점 넷째 자리로 반올림 처리)
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num_1, num_2, num_1 / num_2))
# round 함수 사용 예시 - round(num_1 / num_2, 2) (0.33 소수점 둘째 자리로 반올림)
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, round(num_1 / num_2, 2)))