# 04. 사전 뒤집기

# 참고

# 실습 설명
# 태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다.
# 하지만 이번에는 영-한으로 공부하는 것이 아니라,
# 한-영으로 공부를 해 보고 싶습니다.

# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요.
# reverse_dict는 파라미터로 사전 old_dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.

# 실습 결과
# 영-한 단어장
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명', 'privilege': '특권', 'principles': '원칙'}

# 한-영 단어장
# {'살균제': 'sanitizer', '야망': 'ambition', '양심': 'conscience', '문명': 'civilization', '특권': 'privilege', '원칙': 'principles'}

# 힌트 1 - old_dict의 key와 value를 모두 받아오려면 어떻게 해야 할까요?
#         이렇게 하면 됩니다.
#         for key, value in old_dict.items():

# 힌트 2 - 각 key-value 쌍을 new_dict에 저장하고 싶은 건데요.
#         new_dict[key] = value를 하면 기존 old_dict와 똑같은 사전이 만들어집니다.
#         new_dict[value] = key를 해야 뒤집힌 사전을 만들 수 있겠죠?

# 실습 해설

# 해설
# old_dict의 key와 value를 모두 받아오려면 어떻게 해야 할까요?
# 이렇게 하면 됩니다.

# for key, value in old_dict.items():
# 각 key-value 쌍을 new_dict에 저장하고 싶은 건데요.
# new_dict[key] = value를 하면 기존 old_dict와 똑같은 사전이 만들어집니다.
# new_dict[value] = key를 해야 뒤집힌 사전을 만들 수 있겠죠?

# 모범 답안
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(old_dict):
    new_dict = {}  # 새로운 사전

    # old_dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in old_dict.items():
        new_dict[value] = key

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 코드
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(old_dict):
    new_dict = {}  # 새로운 사전

    # old_dict의 key와 value를 뒤집어서 new_dict에 저장
    # 여기에 코드를 작성하세요
    for key, value in old_dict.items():
        key, value = value, key
        new_dict[key] = value

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))