# 프로그래밍과 데이터 in Python
# 2. for 반복문
# 03. range 연습

# 참고

# 실습 설명
# numbers라는 리스트가 주어졌습니다.

# for문과 range 함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.

# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.
# 실습 결과
# 0 2
# 1 3
# 2 5
# 3 7
# 4 11
# 5 13
# 6 17
# 7 19
# 8 23
# 9 29
# 10 31

# 힌트 1 - 리스트의 길이가 20이라고 가정하면,
#         해당 리스트의 인덱스 목록은 range(20)으로 받아올 수 있습니다.
#         리스트 numbers의 인덱스 목록을 받아오려면 range(len(numbers))를 하면 되겠죠?

# 힌트 2 - numbers의 인덱스만 모두 출력하는 코드를 공개하겠습니다.
#         for i in range(len(numbers)):
#             print(i)
#         인덱스와 원소를 함께 출력하려면 어떻게 해야 할까요?

# 실습 해설

# 해설
# 리스트의 길이가 20이라고 가정하면,
# 해당 리스트의 인덱스 목록은 range(20)으로 받아올 수 있습니다.
# 리스트 numbers의 인덱스 목록을 받아오려면 range(len(numbers))를 하면 되겠죠?

# 우선 인덱스만 순서대로 출력해 봅시다.

# for i in range(len(numbers)):
#     print(i)

# 인덱스 i에 있는 원소를 받아오려면 numbers[i]를 하면 되는데요.
# 그러면 i와 numbers[i]를 함께 출력하면 되겠죠?

# 모범 답안
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])

# 코드
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 여기에 코드를 작성하세요
# for i in range(0, len(numbers)):
for i in range(len(numbers)):
    # print("{} {}".format(i, numbers[i]))
    print(i, numbers[i])