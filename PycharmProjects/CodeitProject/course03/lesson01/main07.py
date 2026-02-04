# 07. 리스트 함수 활용하기

# 참고

# 실습 설명
# 리스트 함수를 활용하여 아래의 지시 사항을 따르세요.

# numbers라는 빈 리스트를 만들고 리스트를 출력한다.
# append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
# numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
# numbers 리스트를 정렬한 후 출력한다.
# 실습 결과
# []
# [1, 7, 3, 6, 5, 2, 13, 14]
# [6, 2, 14]
# [20, 6, 2, 14]
# [2, 6, 14, 20]

# 힌트 1 - 홀수 원소를 제거하는 부분이 살짝 헷갈릴 수 있습니다.
#         많은 분들이 아래 코드처럼 작성하시는데,

#         numbers = [1, 7, 3, 6, 5, 2, 13, 14]  # 예시 리스트
#         i = 0
#         while i < len(numbers):
#             # 홀수면 제거
#             if numbers[i] % 2 == 1:
#                 del numbers[i]
#             i += 1
#         이렇게 하면 문제가 있습니다.

#         numbers[0]은 처음에 1이기 때문에 홀수입니다.
#         그러면 제거가 되겠죠?
#         이제 리스트는 [7, 3, 6, 5, 2, 13, 14]입니다.

#         그 다음 while문의 수행 부분으로 들어갈 때는 i가 1로 바뀐 상태이기 때문에 numbers[1]을 확인하는데요.
#         현재 numbers[1]에 있는 값은 3입니다.
#         우리는 7을 확인하지 못한 채 3을 확인하는 거죠.

#         이 문제를 어떻게 해결해야 할지 잘 생각해 보세요!

# 힌트 2 - 힌트 1에 나와있는 이슈를 해결하려면 어떻게 해야 할까요?
#         어떤 요소가 홀수여서 제거될 경우, 그 뒤에 있는 요소들이 모두 하나씩 앞당겨집니다.
#         예를 들어서 numbers[3]이 홀수여서 제거되면,
#         4번 인덱스에 있던 요소는 3번 인덱스로 가고 5번 인덱스에 있던 요소는 4번 인덱스로 간다는 거죠.

#         우리는 현재 i를 1씩 늘려 주며 while 반복문을 돌고 있는데요.
#         홀수인 요소를 제거하고 나서는 i를 늘리면 안 됩니다.
#         i를 늘리면 요소 하나를 검토하지 않고 건너뛰게 되는 겁니다.

#         수행 부분에서 경우를 나눠서 동작을 다르게 하면 됩니다.
#         홀수 요소를 찾으면 그 요소를 제거하고,
#         짝수 요소를 찾으면 i를 늘리는 거죠. 아래 코드처럼요!

#         numbers = [1, 7, 3, 6, 5, 2, 13, 14]  # 예시 리스트
#         i = 0
#         while i < len(numbers):
#             if numbers[i] % 2 == 1:
#                 del numbers[i]
#         else:
#             i += 1

# 실습 해설

# 해설
# 빈 리스트에 값들 추가
# numbers라는 빈 리스트를 만들어 줍니다.

numbers = []
print(numbers)
# 리스트에 값들 추가
# append를 이용해서 원하는 값들을 순서대로 '추가'하면 됩니다.

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# 홀수 모두 제거
# while 반복문을 이용해서 numbers 리스트의 원소를 순서대로 확인할 수 있습니다.
# 하나씩 보다가 홀수인 원소가 있으면 제거하면 되겠죠?
# 이 논리를 코드로 표현하면 아래와 같습니다.

i = 0
while i < len(numbers):
    # 홀수면 제거
    if numbers[i] % 2 == 1:
        del numbers[i]
    i += 1
print(numbers)

# 그런데 사실 위 코드에는 문제가 있습니다.
# 어떤 요소가 홀수여서 제거될 경우,
# 그 뒤에 있는 요소들이 모두 하나씩 앞당겨집니다.
# 예를 들어서 numbers[3]이 홀수여서 제거되면,
# 4번 인덱스에 있던 요소는 3번 인덱스로 가고 5번 인덱스에 있던 요소는 4번 인덱스로 간다는 거죠.

# 우리는 현재 i를 1씩 늘려 주며 while 반복문을 돌고 있는데요.
# 홀수인 요소를 제거하고 나서는 i를 늘리면 안 됩니다.
# i를 늘리면 요소 하나를 검토하지 않고 건너뛰게 되는 겁니다.

# 수행 부분에서 경우를 나눠서 동작을 다르게 하면 됩니다.
# 홀수 요소를 찾으면 그 요소를 제거하고,
# 짝수 요소를 찾으면 i를 늘리는 거죠.
# 아래 코드처럼요!

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# 인덱스 0 자리에 20을 삽입
# insert를 이용해서 값을 원하는 위치에 '삽입'할 수 있습니다.

numbers.insert(0, 20)
print(numbers)

# 정렬
# sort를 이용해서 리스트를 정렬할 수 있습니다.
# 작은 순서대로 정렬하기 위해서 파라미터를 안 넘겨 줬습니다.

numbers.sort()
print(numbers)

# 모범 답안
# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)
[]
[1, 7, 3, 6, 5, 2, 13, 14]
[6, 2, 14]
[20, 6, 2, 14]
[2, 6, 14, 20]

# 코드
# 빈 리스트 만들기
# 코드를 입력하세요
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    # 인덱스 i는 numbers[i]가 짝수 일 때만 1씩 더해야 한다.
    # 이유는 list의 item 1개를 삭제할 경우 index가 1개씩 당겨진다.

    # 그래서 1개를 지우고 다음 값을 확인하려고 한다면 같은 index 번호로 접근해야 한다.
    # 결과적으로 이 코드에서 i+=1 이라는 게 짝수 일 때만 되어야 하는 것이기 때문에 else를 사용해야 한다.
    if 1 == numbers[i] % 2:  # 홀수일 경우
        del numbers[i]
    else:  # 짝수일 경우
        i += 1  # 인덱스 1 증

# 리스트의 길이가 줄어들면서 인덱스가 꼬일 수 있기 때문에
# 뒤에서부터 리스트 조회해서 삭제하는 구현 방식
# i = len(numbers) - 1
# while i >= 0:
#     if numbers[i] % 2 == 1:
#         del numbers[i]
#     i -= 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)