# 02. 영어 단어장

# 참고

# 실습 설명
# 태호는 미국 다트머스 대학교 컴퓨터 과학과에 지원하려고 합니다.
# 컴퓨터 과학 전공으로 미국 유학을 가고 싶기 때문에,
# 코딩 공부와 영어 공부를 모두 해야 하는 상황인데요.
# 그 둘을 동시에 하기 위해서 파이썬으로 단어장 프로그램을 만들기로 합니다.

# 해야 할 일
# 단어장 만들기
# 새로운 단어들 추가
# 1. 단어장 만들기
# 잘 모르는 단어 네 개입니다.

# sanitizer: 살균제
# ambition: 야망
# conscience: 양심
# civilization: 문명

# 이 단어들을 저장하는 사전을 만들고,
# 만든 사전을 vocab라는 변수에 저장하세요.
# 단어와 뜻이 key-value로 들어가야 합니다.

# 2. 새로운 단어들 추가
# 이미 만들어진 vocab 사전에 새로운 단어들을 추가하고 싶습니다.
# 아래 단어들을 추가해 주세요.

# privilege: 특권
# principle: 원칙

# 실습 결과
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명'}
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명', 'privilege': '특권', 'principle': '원칙'}

# 힌트 1 - 사전을 만들기 위해서는 괄호를 열고 닫고, 그 사이에 원하는 쌍(pair)들을 추가하면 됩니다.
# 힌트 2 - vocab 사전에 새로운 key-value 쌍을 추가하기 위해서는 vocab[key] = value의 형태로 코드를 쓰면 됩니다.

# 실습 해설

# 해설
# 1. 단어장 만들기
# 사전을 만들기 위해서는 괄호를 열고 닫고,
# 그 사이에 원하는 쌍(pair)들을 추가하면 됩니다.

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}

# 2. 새로운 단어들 추가
# vocab 사전에 새로운 key-value 쌍을 추가하기 위해서는
# vocab[key] = value의 형태로 코드를 쓰면 됩니다.

vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

# 모범 답안
# 1. 단어장 만들기
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)

# 코드
# 1. 단어장 만들기
vocab = {
    # 여기에 코드를 작성하세요
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
}
print(vocab)


# 2. 새로운 단어들 추가
# 여기에 코드를 작성하세요
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

print(vocab)