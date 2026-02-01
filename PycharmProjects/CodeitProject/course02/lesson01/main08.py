# 08. format을 이용한 문자열 포매팅

# 참고
# zfill 함수 - 문자열의 빈자리를 0으로 채우는 기능
# 참고 URL - https://docs.python.org/ko/3.13/library/stdtypes.html#str.zfill
# 참고 2 URL - https://stackoverflow.com/questions/339007/how-do-i-pad-a-string-with-zeros?rq=1

# 날짜 계산기(날짜 덧셈 add 함수 포함) 라이브러리 moment
# 참고 URL - https://github.com/zachwill/moment#chaining

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 2019년 10월 29일입니다.")
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")   # 결과값 - 오늘은 2019년 10월 29일입니다.
# 아래에서 설명하는 중괄호({})는 문자열 중간중간에 끼워넣을 수 있는 방법이다.
# 첫 번째 중괄호({}) - year 매핑
# 두 번째 중괄호({}) - month 매핑
# 세 번째 중괄호({}) - day 매핑
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))   # 결과값 - 오늘은 2019년 10월 29일입니다.

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))   # 결과값 - 오늘은 2019년 10월 29일입니다.
print(date_string.format(year, month, day + 1))   # 결과값 - 오늘은 2019년 10월 30일입니다.

_year = 2019
_month = 5
_day = 5

print("오늘은 " + str(_year) + "년" + str(_month) + "월" + str(_day) + "일입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(_year,_month,_day))
# 정수형(int)의 빈자리를 0으로 채울때는 {:02d} 처럼 써주면 된다.
_date_string = "오늘은 {}년 {:02d}월 {:02d}일 입니다."
print(_date_string.format(_year, _month, _day))

# zfill 함수 사용 예시 - 문자열의 빈자리를 0으로 채우는 기능
# 참고 URL - https://docs.python.org/ko/3.13/library/stdtypes.html#str.zfill
# 참고 2 URL - https://stackoverflow.com/questions/339007/how-do-i-pad-a-string-with-zeros?rq=1
z_year = 2020
z_month = "5".zfill(2)   # 문자열 길이(width) 2로 만들기 위해 "0" 문자열을 왼쪽에 채우기
z_day = 11

print("오늘은 {}년 {}월 {}일입니다.".format(z_year, z_month, z_day))


# 날짜 자동 계산기
c_year = 2019
c_month = 10
c_day = 29

def cg(y, m, d):
    """
    Description: [테스트] 날짜 자동 계산기

    Parameters: y - 년도
                m - 월
                d - 일

    Returns: y, m, d - 년도, 월, 일
    """

    if d > 31:   # 31일 초과
        m = m + 1
        d = d - 31
    if m > 12:   # 12월 초과
        m = 1
        y = y + 1
    return y, m, d

c_year, c_month, c_day = cg(c_year, c_month, c_day + 5)

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(c_year, c_month, c_day))
