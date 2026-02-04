# 07. 팰린드롬

# 참고
# 파이썬 join 함수(리스트 -> 문자열 변환)
# 참고 URL - https://docs.python.org/ko/3.13/library/stdtypes.html#str.join
# 참고 2 URL - https://velog.io/@thguss/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8list%EB%A5%BC-%EB%AC%B8%EC%9E%90%EC%97%B4string%EB%A1%9C-%EB%B3%80%ED%99%98

# 실습 설명
# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.

# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요.
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.

# 예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 합니다.
# 그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 거죠.

# 실습 결과
# True
# False
# True
# True
# False

# 힌트 1 - 문자열의 첫 번째 원소와 마지막 원소를 비교해서 일치하는지 확인해야 합니다.
#         그 다음 문자열의 두 번째 원소와 끝에서 두 번째 원소를 비교해서 일치하는지 확인해야겠죠.
#         이런 식으로 순서대로 비교하는 건데요.
#         한 쌍이라도 일치하지 않으면 False를 리턴하고,
#         모든 쌍이 일치하는 경우 True를 리턴하면 되겠죠?

# 힌트 2 - 문자열 word의 첫 번째 원소의 인덱스는 0이고,
#         마지막 원소의 인덱스는 len(word) - 1입니다.
#         문자열 word의 두 번째 원소의 인덱스는 1이고,
#         끝에서 두 번째 원소의 인덱스는 len(word) - 2입니다.

#         이걸 어떻게 일반화할 수 있을까요?
#         인덱스 i에 있는 값과 인덱스 len(word) - i - 1에 있는 값을 비교하면 됩니다!

# 실습 해설

# 해설
# 문자열의 첫 번째 원소와 마지막 원소를 비교해서 일치하는지 확인해야 합니다.
# 그 다음 문자열의 두 번째 원소와 끝에서 두 번째 원소를 비교해서 일치하는지 확인해야겠죠.

# 문자열 word의 첫 번째 원소의 인덱스는 0이고,
# 마지막 원소의 인덱스는 len(word) - 1입니다.
# 문자열 word의 두 번째 원소의 인덱스는 1이고,
# 끝에서 두 번째 원소의 인덱스는 len(word) - 2입니다.

# 이걸 어떻게 일반화할 수 있을까요?

# i를 0부터 1씩 늘린다고 가정했을 때,
# 인덱스 i에 있는 값과 인덱스 len(word) - i - 1에 있는 값을 비교하면 됩니다!

# 참고로 i를 0부터 len(word) - 1까지 반복할 필요는 없습니다.
# 어차피 반대쪽과 비교하는 것이기 때문에 i를 len(word) // 2까지만 반복해도 이미 모든 확인은 끝나는 거죠!

# 모범 답안
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

# 코드
def is_palindrome(word):
    """
    Description: 팰린드롬(palindrome) 단어 여부 확인

    Parameters: word - 단어가 저장된 문자열

    Returns: True - 팰린드롬(palindrome) 단어일 경우
             False - 팰린드롬(palindrome) 단어 아닌 경우
    """

    # 여기에 코드를 작성하세요
    word_list = list(word)

    for left in range(len(word_list) // 2):
        right = len(word) - left - 1
        word_list[left], word_list[right] = word_list[right], word_list[left]

    # print(''.join(word_list))

    if ''.join(word_list) == word:
        return True
    else:
        return False


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))