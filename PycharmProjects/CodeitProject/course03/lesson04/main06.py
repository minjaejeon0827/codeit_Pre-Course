# 프로그래밍과 데이터 in Python
# 4. 파이썬 데이터의 비밀
# 06. 주민등록번호 가리기

# 참고


# 실습 설명
# 주민등록번호 YYMMDD-abcdefg는 총 열세 자리인데요.

# 앞의 여섯 자리 YYMMDD는 생년월일을 의미합니다.

# YY → 연
# MM → 월
# DD → 일
# 뒤의 일곱 자리 abcdefg는 살짝 복잡합니다.

# a → 성별
# bc → 출생등록지에 해당하는 지방자치단체의 고유번호
# defg → 임의의 번호
# 보시다시피 많은 부분은 특정 규칙대로 정해져 있는데요.
# 여러분에 대한 몇 가지 정보만 알면,
# 마지막 네 개 숫자 defg를 제외한 앞의 아홉 자리는 쉽게 알 수 있다는 거죠.

# 그래서 저희는 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 합니다.

# mask_security_number라는 함수를 정의하려고 하는데요.
# 이 함수는 파라미터로 문자열 security_number를 받고,
# security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.

# 참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.
# 작대기 포함 여부와 상관 없이,
# 마지막 네 글자가 '*'로 대체되어야 합니다!

# 실습 결과
# 880720-123****
# 880720123****
# 930124-765****
# 930124765****
# 761214-235****
# 761214235****

# 힌트 1 - 문자열은 수정이 불가능합니다.
#         하지만 문자열과 유사한 리스트는 수정이 가능하죠?
#         그러면 문자열 security_number를 리스트로 변환한 후,
#         마지막 네 원소를 '*'로 바꿔 주면 됩니다.
#         그리고 나서 그 리스트를 다시 하나의 문자열로 합치면 되겠죠?

# 힌트 2 - 사실 더 쉬운 방법이 있습니다.
#         문자열 슬라이싱을 이용하는 건데요.
#         security_number의 마지막 네 자리만 제외해서 슬라이싱을 하고, 문자열 "****"과 연결하면 끝입니다!

# 실습 해설

# 해설
# 접근법 #1
# 문자열은 수정이 불가능합니다.
# 하지만 문자열과 유사한 리스트는 수정이 가능하죠?
# 그러면 문자열 security_number를 리스트로 변환한 후,
# 마지막 네 원소를 '*'로 바꿔 주면 됩니다.
# 그리고 나서 그 리스트를 다시 하나의 문자열로 합치면 되겠죠?

# 코드로 봅시다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = []
    for i in range(len(security_number)):
        num_list.append(security_number[i])

# 문자열을 반복문을 쓰지 않고 한번에 리스트로 바꾸고 싶으면 곧바로 형 변환을 쓸 수도 있습니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

# 이제 마지막 네 요소, 즉 인덱스 len(num_list) - 4부터 인덱스 len(num_list) - 1의 값들을 *로 바꿔주면 됩니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

# 마지막으로 이 리스트를 이제 다시 문자열로 만들어서 리턴시켜 주어야합니다.
# 리스트의 각 요소를 하나씩 빈 문자열을 시작으로 연결해주면 기존 문자열로 만들 수 있을 것입니다.
# 그럼 이 연결을 어떻게 해줄 수 있을까요?
# 리스트와 문자열 정리에서 배운 덧셈 연산을 이용하면 됩니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str

# 접근법 #2
# 사실 리스트를 문자열로 복구하는 코드는 join() 이라는 메소드로 한번에 할 수 있습니다.
# 이 메소드는 문자열로 이루어진 리스트를 구분자로 결합하여 하나의 문자열로 만들어 줍니다.
# 아래 코드로 확인해보겠습니다.

units = ["cm", "m", "yard"]
units_to_string = ', '.join(units)

print(type(units_to_string))
print(units_to_string)
# <class 'str'>
# cm, m, yard
# join() 메소드는 str.join(list) 형태로 쓰게 됩니다.
# str은 리스트 요소들을 결합할 때 사용될 구분자입니다.
# 구분자는 문자열이어야 합니다.
# 그리고 list 는 각 요소가 문자열인 리스트를 의미합니다.
# 그래서 위 코드의 결과로 units 리스트의 각 요소들이 ,와 공백으로 결합된 하나의 문자열로 출력되는 것입니다.

# 이 과제에서는 각 숫자들을 공백없이 결합을 해야합니다.
# 그럼 어떻게 작성할 수 있을까요?
# 잠시 생각해보시고 아래 코드를 확인해보세요.

def mask_security_number(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list)

# 접근법 #3
# 그런데 더 쉬운 방법이 있습니다. 문자열 슬라이싱을 이용하는 건데요.

# security_number의 마지막 네 자리만 제외해서 슬라이싱을 하고,
# 문자열 "****"과 연결하면 끝입니다!

# 모범 답안
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

# 코드
def mask_security_number(security_number):
    """
    Description: 주민등록번호 뒷 4자리 마스킹 처리

    Parameters: security_number - 주민등록번호 문자열

    Returns: mask_number - 마스킹 처리 완료된 주민등록번호
    """

    # 여기에 코드를 작성하세요
    mask_number = security_number[:-4] + "****"
    return mask_number


# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))