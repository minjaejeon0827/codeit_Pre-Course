# 프로그래밍 핵심 개념 in Python
# 2. 추상화
# 05. return과 print의 차이 실습

# 참고

# 실습 설명
# 각 함수의 message 변수에 "코드잇", "codeit", None 이 할당되어 있습니다.
# 다음 주어진 두 코드 중 하나를 각 함수 내부에 추가하여 하단의 실습 결과와 같아지도록 만들려고 합니다.

# print(message)
# return message
# 먼저,

# 각 함수의 message 변수에 할당된 값에 따라 어떤 값을 출력하거나 반환할 수 있는지 생각해 보고,
# 실습 결과의 문자열과 실행기 # 테스트 코드에 주어진 각 함수의 가능한 호출 결과를 서로 비교하며 하나씩 함수를 완성해 보세요
# 주어진 print 함수와 return 문을 코드를 추가하는 것 이외에 실행기의 테스트 코드나 message 에 할당된 값은 변경하지 마세요.

# 실습 결과
# 코드잇
# codeit
# None
# None

# 실습 해설
#
# 해설
# return과 print의 차이는 프로그래밍을 처음 배울 때 많이 혼동하는 것 중 하나예요.
# 이번 실습과 해설을 통해 어떤 차이가 있는지 이해해 볼게요.
#
# 먼저 다음 내용을 기억해 주세요.
#
# 함수는 호출된 후 항상 값을 반환해요
# return 문에 반환할 값이 명시되지 않으면 None을 반환해요.
#
# 반환할 값을 명시했을 때

def return_message():
    return "안녕하세요"

# return_message()
#
# 반환할 값을 명시할 때 return 문을 사용해요.
# 위 코드에서는 return_message() 함수를 호출하면
# 반환하도록 명시한 "안녕하세요" 라는 문자열을 함수를 호출한 자리로 돌려줘요.
#
# 반환할 값을 명시하지 았았을 때

def return_nothing():
    message = "안녕하세요"


return_nothing()

# 위 코드에는 값을 반환하기 위한 return 문이 없어요.
# 이런 경우 None을 함수를 호출한 자리로 돌려줘요.

def return_nothing():
    return


# return_nothing()
# 위 코드는 어떨까요?
# return 문이 쓰였지만 반환할 값이 명시되어 있지 않아요.
# 이때에도 None을 반환해요.
#
# "반환하다" VS "출력하다"
# return 과 print 차이를 이해하기 위해서는 각각의 역할을 정확히 이해해야 해요.
#
# return 문은 값을 호출한 자리에 반환해줘요
# print 함수는 주어진 인수를 출력해줘요.
# 코드를 통해 확인해 볼게요.
#
# 반환하다
def return_message():
   return "안녕하세요"

return_message()

# 파이썬 인터프리터[1]가 코드를 위에서부터 아래로 해석해요.
# 하지만 1번째 줄에서는 함수 정의만 이루어지고, return "안녕하세요" 코드 실행은 5번째 줄의 return_message()에 의해 이루어져요.
# return_message() 함수를 호출하면 정의한 return_message 함수를 찾아 함수 본문을 실행하는 거예요.
#
# 그래서  return "안녕하세요" 실행 결과로 "안녕하세요"라는 문자열을 호출한 자리에 반환해요.
#
# 즉, 아래와 같다고 생각하시면 돼요.
#
# "안녕하세요"
# 그런데 "안녕하세요" 문자열을 직접 확인할 수는 없어요. 반환을 했을 뿐 출력을 하지 않았기 때문이에요.
#
# 출력하다
# 출력 역할은 print() 함수가 해요. print() 함수를 호출하면 괄호 안의 인수를 평가한 결괏값을 출력해 줘요.

message = "codeit"

print(message)
# 위 코드에서 print() 함수의 인수로는 message라는 변수가 쓰였어요.
# 그럼 print() 함수는 이 message라는 변수를 평가하여 message 변수에 할당된 "codeit"이라는 문자열을 출력하게 돼요.
#
# 그렇다면 함수 본문을 수정하지 않고, "안녕하세요" 를 출력하기 위해서는 어떻게 해야 할까요?
# 출력을 하기 위해선 print() 함수를 이용하면 되고,
# print() 함수의 인수로 "안녕하세요" 를 넣어 호출하면 돼요.
#
# 다시 말하면,

print("안녕하세요")
# 함수 호출 결과로 위와 같게 만들면 되는 거예요.
#
# return_message() 함수를 호출한 결괏값이 호출한 자리에 반환된 "안녕하세요"이니 아래와 같이 작성하면 "안녕하세요"가 출력돼요.

def return_message():
   return "안녕하세요"

print(return_message())
# 물론, 다음과 같이 return_message()함수 본문에 return 대신 print() 함수를 쓸 수도 있어요.

def return_message():
   print("안녕하세요")

return_message()
# return_message() 함수 호출로 "안녕하세요" 가 출력되고 return 문이 없으니 결괏값으로 None 이 반환돼요.
# 하지만 이 None 을 출력하기 위한 print() 함수가 없어서 None 은 출력되진 않아요.

# 실습 살펴보기
# 함수는 호출된 후 항상 값을 반환해요.
# return 문에 반환할 값이 명시되지 않으면 None 을 반환해요.
# 처음에 언급했던 문장을 다시 한번 기억하면서 실습을 살펴볼게요.

def first():
    message = "코드잇"


def second():
    message = "codeit"


def third():
    message = None


# 테스트 코드
print(first())
second()
print(third())
# 각 함수를 보면 return 문이 없어요.
# 실습 요구사항대로 함수 본문을 작성하기 전에 이대로 실행하면 어떤 값이 출력될지도 알아볼게요.
# 아래 내용을 보기 전에 먼저 생각해 보셔도 좋아요.

def first():
    message = "코드잇"


# 테스트 코드
print(first())
# first() 함수를 호출하면 None 을 호출한 자리로 반환해 줘요.

# 테스트 코드
print(None)

# 그래서 함수 호출 결과 위와 같다고 할 수 있고,
# print() 함수의 인수로 None 이 있으니 None 을 출력해 줍니다.

def second():
    message = "codeit"


# 테스트 코드
second()
# 역시 return 문이 없으므로 None 을 반환해요.
# 그럼 함수 호출 후에 아래와 같을 거예요

# 테스트 코드
None
# 그런데 이 None 은 함수 호출 결과로 반환되었을 뿐이에요.
# 그래서 None 이 출력되진 않아요.
# 출력을 하기 위한 print() 함수가 쓰이지 않았으니까요.

# third() 함수 부분은 first() 함수 설명과 동일하므로 생략할게요.
#
# 이제 실습 요구사항대로 코드를 작성해 볼게요.
#
# 코드잇
# codeit
# None
# None
# 실습을 하실 때는 가장 먼저 실습의 요구 사항을 충분히 이해하고 넘어가 주세요.
# 종이에 요구 사항과 함께 어떻게 해결할지를 적으면서 생각해 보시는 것도 추천드려요.

# 이 실습에서는 함수 본문에 return message 또는print(message) 를 추가하여 위 결과가 출력되도록 만들어야 해요.
# 다른 코드는 추가하거나 수정해서는 안 돼요.
#
# "코드잇" 문자열부터 보면, first() 함수 본문의 message 변수에 할당되어 있어요.
# 그러므로 함수 호출결과로 이 message 변수를 반환하도록 하고, 이 반환한 결괏값을 출력하면 됩니다.

def first():
    message = "코드잇"


# 테스트 코드
print(first())
# 테스트 코드를 보면 first() 함수를 호출한 결괏값을 print() 함수가 출력하도록 되어 있어요.
# 그러므로 print(first())가 print("코드잇")이 되게 만들면 돼요.
# 다음과 같이 message 변수를 반환하도록 return message 를 본문에 추가하면 "코드잇"이 출력돼요.

def first():
    message = "코드잇"
    return message

# 테스트 코드
print(first())
# 다음은 second() 함수를 호출한 결과로 "codeit" 이 출력되게 만들어야 해요.

def second():
    message = "codeit"


# 테스트 코드
second()
# 그런데 호출 부분을 보면 print() 함수가 없어요.
# 함수 본문에만 코드를 추가할 수 있으니 "codeit" 이 출력되게 하려면 아래와 같이 함수 본문에서 "codeit" 을 출력하게 해야 해요.

def second():
    message = "codeit"
    print(message)


# 테스트 코드
second()

# 마지막으로 None 이 두 번 출력되게 해야 해요.

def third():
    message = None


# 테스트 코드
print(third())
# 코드를 살펴보면 print() 함수가 third() 함수를 호출한 결괏값을 출력해줘요.
# 어떤 코드를 추가하지 않아도 이 코드를 실행하면 return 문이 없어서 None 을 반환하고,
# print(None)이 되어  None 이 출력돼요.

# 테스트 코드
print(None)

# 하지만 실습 결과를 보면 None이 두 번 출력되게 만들어야 해요.
# message를 return 하면 어떻게 될까요?

def third():
    message = None

    return message


# 테스트 코드
print(third())
# 실행 결과
None
# None은 출력되지만 역시 한 번만 출력돼요.
#
# 아래와 같이 함수 본문에서 message 변수에 할당된 None을 출력하게 만들면 어떻게 될까요?

def third():
    message = None
    print(message)


# 테스트 코드
print(third())
# third() 함수를 호출하면 함수 본문이 실행돼요.
# 그래서 print(message) 에 의해 None 이 한번 출력돼요.
# 그리고 함수에 return 이 없으므로 None 이 호출한 결괏값으로 반환이 돼요.

# 테스트 코드
print(None)
# 그러므로 두 번째 None 이 출력되는 거예요.

# 실행 결과
None
None

# 모범 답안
def first():
    message = "코드잇"
    return message


def second():
    message = "codeit"
    print(message)


def third():
    message = None
    print(message)