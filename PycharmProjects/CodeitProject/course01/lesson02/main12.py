# 12. 프로그래밍 기초 퀴즈
# 변수: 값을 저장하는 역할
# 함수: 명령을 저장하는 역할
# 파라미터: 함수에 넘거주는 (인자)값
# return문: 함수에게 뭔가 정보를 주면 어떤 다른 정보를 돌려준다.

# return vs print 함수 차이
# return : 함수의 결과값을 가지고 있음. 합수의 결과값을 함수 밖에서 사용 가능
# print : 함수의 결과값을 표시만 함. 함수의 결과값을 함수 밖에서 사용 불가능

# 함수 매개변수와 인수
# 참고 URL - https://wikidocs.net/24#_4
# 참고 2 URL - https://www.codeit.kr/community/threads/10416
# 참고 3 URL - https://www.codeit.kr/community/threads/5998
# 참고 4 URL - https://mingrammer.com/understanding-the-asterisk-of-python/

# math.prod 함수 - 이터러블(iterable) 객체(튜플, 리스트 등등...)에 속한 모든 요소 곱하기
# 참고 URL - https://docs.python.org/ko/3/library/math.html#math.prod

# 질문 1 30 XP
# 다음 코드를 실행한 출력 결과를 예상해 보세요.
# 정답: 13
# 해설: a는 숫자형 5, b는 숫자형 8입니다. 따라서 두 값을 합치면 숫자형 13이 나옵니다.
# a = 5
# b = 8
# c = "5"
# d = "8"
#
# print(a + b)

# 질문 2 30 XP
# 다음 코드를 실행한 출력 결과를 예상해 보세요.
# 정답: "58"
# 힌트 1: "으로 둘러싸인 자료형은 숫자가 아닌 문자입니다.
# 힌트 2: 문자와 문자의 + 연산 결과는, 두 문자를 이은 문자가 됩니다.
# 해설: c는 문자열 "5", d는 문자열 "8"입니다.
#      문자열을 더하면, 문자열을 이어 연결하는 것과 같은데요.
#      따라서 "5"와 "8"이 연결된 "58"이 나옵니다.
a = 5
b = 8
c = "5"
d = "8"

print(c + d)

# 질문 3 30 XP
# 다음 코드를 실행한 출력 결과를 예상해 보세요.
# 정답: 40
# 해설: 파라미터 x에 정수 10이 넘어가고, 파라미터 y에 정수 20이 넘어갑니다.
#      my_function 함수는 x + x + y를 리턴하기 때문에 10 + 10 + 20의 결괏값인 40이 리턴되겠죠?
#      그러면 리턴값인 40이 함수 호출 부분을 대체해서, 마지막 줄은 print(40)이 됩니다.
#      그래서 40이 출력되는 거죠.

def my_function(x, y):
    return x + x + y

print(my_function(10, 20))
