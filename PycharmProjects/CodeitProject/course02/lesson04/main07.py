# 프로그래밍 핵심 개념 in Python
# 4. 문제 해결 능력 기르기
# 07. 피보나치 수열

# 참고
# [반복문에서 Python Tutor 활용하기 in Python]
# 참고 URL - https://www.codeit.kr/tutorials/92/using-python-tutor-with-loops-in-python

# 의사코드(pseudo-code)란?
# 참고 URL - https://medium.com/djangogirlsseoul-codecamp/%EC%9D%98%EC%82%AC%EC%BD%94%EB%93%9C-pseudo-code-%EB%9E%80-d892a3479b1d

# 프로그래밍 핵심 개념 in Python 예제 실습
# 참고 URL - https://www.codeit.kr/topics/practice-core-concept-of-python-programming

# (코드잇) 파이썬 피보나치 수열
# 유튜브 참고 URL - https://www.youtube.com/watch?v=FSsvY5Ki8_A

# 실습 설명
# 피보나치 수열(Fibonacci Sequence)이라고 들어 보셨나요?

# 1,1,2,3,5,8,13,21,34,55,...

# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다.
# 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다.
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며,
# 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.

# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성해 보세요.

# 실습 결과
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# .
# .
# .
# 4807526976
# 7778742049
# 12586269025

# 힌트 1 - 일단 50개의 항이 조금 부담될 수 있으니,
#         10개의 항만 출력하는 것을 목표로 합시다.
#         어차피 10개를 제대로 출력할 수 있으면,
#         50개도 아무런 문제없이 출력할 수 있을 테니까요.

#         10개의 항을 출력하기 위해서는 반복문을 열 번 돌아야겠죠? 열 번 도는 반복문부터 작성해 봅시다.
#
#         i = 1
#         # 추가적으로 필요한 변수가 몇 개 더 있습니다

#         while i <= 10:
#             # 우리가 반복적으로 무엇을 해야 할까요?
#             i += 1
#         이제 여기서 발전시켜 보세요.

# 힌트 2 - 피보나치 수열의 항은 앞선 두 항의 합으로 계산되는데요.
#         따라서 피보나치 수열의 항들을 순서대로 출력하기 위해서는 늘 마지막 두 항을 변수에 보관해야 합니다.

#         '현재 항'은 변수 current에, 그리고 '직전 항'은 변수 previous에 저장을 하겠습니다.
#         처음에는 current를 1로 설정하고 previous를 0으로 설정하면 되겠죠?
#
#         previous = 0
#         current = 1
#         i = 1
#
#         while i <= 10:
#             # 우리가 반복적으로 무엇을 해야 할까요?
#             i += 1
#         이제 while 반복문의 수행 부분만 채워 넣으면 됩니다.

# 힌트 3 - 수행 부분에서 해야 할 일은 크게 두 가지입니다.

#         current를 출력
#         previous와 current를 적절히 수정
#         첫 번째는 그냥 print(current)를 하면 되고,
#         두 번째가 조금 어려울 수 있는데요. 한 번 고민해 보세요.

#         previous = 0
#         current = 1
#         i = 1

#         while i <= 10:
#             print(current)
#             # previous와 current를 적절히 수정
#             i += 1

# 힌트 4 - 수행 부분에서 previous와 current를 어떻게 수정할 수 있을까요? 이렇게 하면 됩니다.
#         previous ← current
#         current ← current + previous
#         코드로 나타내면 그냥 이렇게 하면 되겠죠?

#         previous = current
#         current = current + previous
#         그런데 사실 위 코드처럼 작성하면 문제가 생깁니다. 잘 생각해 보세요. previous = current를 하면, previous와 current가 같은 값을 저장하게 됩니다. 그리고 기존의 previous 값은 잃어버리게 되죠. 그래서 current = current + previous를 하면 current = current + current를 하는 것과 같게 됩니다.

#         이 문제는 어떻게 해결할 수 있을까요?

# 힌트 5 - 힌트 4에서 이야기한 문제점은 기존 previous의 값을 잃어버린다는 것인데요. 이 문제를 해결하기 위해서 임시 보관소 역할을 할 변수를 만들면 됩니다.

#         temp = previous  # previous를 임시 보관소 temp에 저장
#         previous = current
#         current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
#         이렇게 하면 문제없이 previous와 current를 수정할 수 있습니다.

# 실습 해설

# 해설
# 일단 50개의 항이 조금 부담될 수 있으니, 10개의 항만 출력하는 것을 목표로 합시다.
# 어차피 10개를 제대로 출력할 수 있으면, 50개도 아무런 문제없이 출력할 수 있을 테니까요.

# 반복문 틀 작성
# 10개의 항을 출력하기 위해서는 반복문을 열 번 돌아야겠죠?
# 열 번 도는 반복문부터 작성해 봅시다.

i = 1

while i <= 10:
    i += 1

# 필요한 변수 정의
# 피보나치 수열의 항은 앞선 두 항의 합으로 계산되는데요.
# 따라서 피보나치 수열의 항들을 순서대로 출력하기 위해서는 늘 마지막 두 항을 변수에 보관해야 합니다.

# '현재 항'은 변수 current에, 그리고 '직전 항'은 변수 previous에 저장하겠습니다.
# 처음에는 current를 1로 설정하고 previous를 0으로 설정하면 되겠죠?

previous = 0
current = 1
i = 1

while i <= 10:
    # 우리가 반복적으로 무엇을 해야 할까요?
    i += 1

# 이제 while 반복문의 동작 부분만 채워 넣으면 됩니다.

# 동작 부분 채워 넣기
# 동작 부분에서 해야 할 일은 크게 두 가지입니다.

# current를 출력
# previous와 current를 적절히 수정
# 첫 번째 내용은 그냥 print(current)를 하면 되니까 먼저 채워 넣겠습니다.

previous = 0
current = 1
i = 1

while i <= 10:
    print(current)
    # previous와 current를 적절히 수정
    i += 1

# previous와 current 수정하기
# 두 번째가 약간 헷갈리는 부분인데요.
# 동작 부분에서 previous와 current를 어떻게 수정할 수 있을까요?
# 일단 단순하게 생각하면 이렇습니다.

# previous ← current
# current ← current + previous
# 그리고 위 로직을 코드로 나타내면 아래와 같습니다.

# previous = current
# current = current + previous
# 그런데 사실 위 코드처럼 하면 문제가 생깁니다. 코드의 순서대로 한번 따라가 볼게요.
# previous = current를 하면, previous와 current가 같은 값을 저장하게 됩니다.
# 그리고 기존의 previous 값은 잃어버리게 되죠.

# 예를 들어서 previous가 정수 2고 current가 정수 3이라고 생각해 보세요.
# previous = current를 하면 어떻게 되나요?
# previous는 정수 3으로 바뀌고,
# current도 정수 3이죠?
# 기존 previous에 있던 정수 2는 완전히 잃어버리게 됩니다.

# 이 문제를 해결하기 위해서,
# 임시 보관소 역할을 할 변수를 만들어야 합니다.

temp = previous  # previous를 임시 보관소 temp에 저장
previous = current
current = current + temp  # temp에는 기존 previous 값이 저장돼 있음

# 이렇게 하면 이제 문제없이 previous와 current를 수정할 수 있습니다. 코드를 실행하면 아래와 같이 출력이 될 텐데요.

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 이제 while i <= 10:을 while i <= 50:으로 수정하기만 하면 됩니다.

# 모범 답안
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1

# 참고 사항
# 참고로 이 코드를 더 깔끔하게 쓰는 방법이 있는데요. 아래 코드를 봐 주세요.

previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1

# 훨씬 낫죠? 그런데 제가 굳이 temp를 사용하는 방식을 먼저 말씀드린 이유가 있습니다.

# 저렇게 한 줄로 깔끔하게 쓸 수 있는 것은 파이썬에서 제공되는 멋진 문법인데요.
# 코드가 깔끔해지기 때문에 저도 웬만하면 이렇게 작성합니다.
# 하지만 이건 대부분 프로그래밍 언어에서 제공되지 않는 문법입니다.
# 여러분이 이 방식만 배우면, 다른 프로그래밍 언어로는 이 같은 문제를 풀지 못할 수도 있다는 거죠.
# 반면 temp 같은 임시 보관소를 사용하는 방법은 어떤 언어에도 적용 가능하다는 장점이 있습니다.

# 그래도 파이썬에서 유용하게 쓸 수 있는 문법임에는 틀림이 없습니다.
# 이 토픽에서는 프로그래밍에서 전반적으로 쓰는 개념들에 집중하고,
# 다른 과제에서 위 방법에 대해 좀 더 살펴보겠습니다.

# 코드
# 여기에 코드를 작성하세요
dp = [0] * 51
dp[1] = 1
dp[2] = 1
print(dp[1])
print(dp[2])
i = 3

while i <= 50:
    dp[i] = dp[i-1] + dp[i-2]  # 점화식
    print(dp[i])
    i += 1