# 12. 불 대수

# 참고
# 명제란?
# 참 또는 거짓이 확실한 문장

# 불 대수(Boolean Algebra)
# - 일상적인 논리를 수학적으로 표현한 것
# - 불 대수에서 사용하는 값들은 숫자가 아니라 진리값이다.
#   여기서 말하는 진리값이란 어떤 명제가 참인지 거짓인지 나타내는 거라서
#   가능한 값이 True와 False 딱 2가지 뿐이다.
# - 불 대수에서 사용하는 연산들은 숫자 사칙연산(+, -, *, /, %, // 등등...)과 다르게 AND, OR, NOT 이렇게 존재한다.

# AND 연산 - 명제 x AND 명제 y
# - 두 명제가 모두 참(True)이어야 명제 x AND 명제 y 값은 참(True)이다.
# - 두 명제중 하나라도 거짓(False)이면 명제 x AND 명제 y 값은 거짓(False)이다.
# True AND True -> True
# False AND True -> False
# True AND False -> False
# False AND False -> False
# (예) 대한민국의 수도는 서울이다. AND 2는 1보다 크다. - True AND True -> True
# (예) 대한민국의 수도는 서울이다. AND 2는 1보다 작다. - True AND False -> False

# OR 연산 - 명제 x OR 명제 y
# - 두 명제중 하나라도 참(True)이면 명제 x OR 명제 y 값은 참(True)이다.
# - 두 명제가 모두 거짓(False)이어야 명제 x OR 명제 y 값은 거짓(False)이다.
# True OR True -> True
# False OR True -> True
# True OR False -> True
# False OR False -> False
# (예) 대한민국의 수도는 제주도다. OR 대한민국의 수도는 서울이다. -> 명제 결론: 대한민국의 수도는 제주도거나 서울이다. -> False OR True -> True
# (예) 대한민국의 수도는 제주도다. OR 대한민국의 수도는 부산이다. -> 명제 결론: 대한민국의 수도는 제주도거나 부산이다. -> False OR False -> False

# NOT 연산 - NOT 명제 x
# 기존 명제의 진리값을 반대로 뒤집어 주는 역할이다.
# - 명제가 참(True)이면 거짓(False)으로 만들어준다.
# - 명제가 거짓(False)이면 참(True)으로 만들어준다.
# NOT True -> False
# NOT False -> True
# (예) NOT 대한민국의 수도는 서울이다. -> 명제 결론: 대한민국의 수도는 서울이 아니다. -> NOT True -> False
# (예) NOT 2는 1보다 작다. -> 명제 결론: 2는 1보다 작지 않다.(크거나 같다.) -> NOT False -> True

# 비트 연산자와 논리연산자 차이
# 비트연산자는 말 그대로 0 또는 1의 결과값을 가지고 비트 단위의 연산을 하기 위한 것이고,
# and 나 or 같은 논리연산자는 True, False와 같은 논리값 연산을 위한 것이다.
# 그 목적에 따라 써주지 않으면 다른 결과를 발생시킬 수 있다.

# 불 대수와 불린의 차이
# 수학이나 전산학에서 사용하는 불 대수 (참, 거짓)을 표현하기 위한 자료형이 '불린형' (boolean type) 이라고 이해하면 된다.
# 표준 C언어에는 boolean 타입이 없기 때문에 0(정수), '\0'(문자), NULL(포인터) 등이 '거짓'을 대신합니다.
#include <stdio.h>

# int main() {
#
#     if (1) {
#         printf("Hello, C!\n");
#     }
#     while (0) {
#         printf("이 while문은 실행될 일이 없습니다.");
#     }
#
#     return 0;
# }

# 반면 대부분의 언어에서는 boolean 타입을 지원합니다. Python의 경우를 볼까요?
# true_variable = True
# false_variable = False

# if true_variable:
#     print('Hello, Python!')

# while false_variable:
#     print('이 while문 또한 실행되지 않습니다.')

# 이처럼 불 대수를 표현하는 것이 '불린형' 변수라고 볼 수 있다.
# C의 경우처럼 불 대수를 꼭 불린형 변수로 표현해야 하는 것은 아닙니다.
# 비유하자면 한국어를 가장 잘 표현하는 것은 한글이지만, 알파벳이나 한자로도 표현할 수 있는 것처럼요!
