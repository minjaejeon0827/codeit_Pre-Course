# 프로그래밍 시작하기 in Python
# 2. 프로그래밍 기본 개념
# 03. 추상화 개요

# 프로그래밍에서 추상화 3 단계 나누기
# 1 단계: 변수(Variable)
# 2 단계: 함수(Function)
# 3 단계; 객체(Object)
x = 254   # 변수 x는 254 라는 값 저장
y = 317   # 변수 y는 317 라는 값 저장
print(x + y)   # 변수 x, y에 저장된 각각의 값 더하기
print(x + y == 300)   # False
# 오류 메시지 "TypeError: 'x' is an invalid keyword argument for print()" 출력
# 오류 사유: print 내장함수의 경우 parameter로 x와 y를 받고 있지 않음.
# print(x=259, y= 12)   # 오류 메시지 "TypeError: 'x' is an invalid keyword argument for print()" 출력

# python에서 이미 정의되어 제공되는 함수를 내장 함수라고 표현한다.
print("Hello World")   # print 내장 함수 - 괄호 안에 있는 값들을 콘솔(Console) 창 출력 해주는 함수

# 참고사항 - 개발자는 print() 함수가 내부적으로 어떻게 동작하는지 자세히는 모른다.
# 다만, 이런 내부적인 걸 몰라도 아무 문제 없이 사용할 수 있다는 게  추상화(Abstraction)의 장점이자 목적이다.

def compensation(wage, hour):
    """
    :Description: 시간 당 급여 계산

    :Parameters: wage - 임금
                hour - 총 근무시간
    :Returns: None
    """

    exchange = 1142.16

    print(f"{wage}시간에 {wage * hour * exchange:.2f}원 벌었습니다. 시간 당 급여는 {wage * exchange:.2f}원입니다.")

def round_compensation(wage, hour):
    """
    :Description: 시간 당 급여 계산 (round 함수 사용)
                  round 함수는 소수점 이하 끝자리 0을 절삭함.
                  참고 URL
                  https://python.flowdas.com/tutorial/floatingpoint.html
                  https://blog.winterjung.dev/2020/01/06/floating-point-in-python

    :Parameters: wage - 임금
                hour - 총 근무시간
    :Returns: None
    """

    exchange = 1142.16

    print("{}시간에 {}원 벌었습니다. 시간 당 급여는 {:.2f}원입니다.".format(wage, round(wage * hour * exchange, 2), round(wage * exchange, 2)))


# 정답 출력
compensation(3, 4)
compensation(4, 5)
round_compensation(3, 4)
round_compensation(4, 5)