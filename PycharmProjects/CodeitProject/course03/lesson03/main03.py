# 03. 사전 활용법

# 참고

my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

# my_family 사전(dictionary)에 어떤 값(value)들이 있는지 목록 출력
print(my_family.values())
# '이지영' 이라는 값이 있는지 확인
print('이지영' in my_family.values())  # 결과값: True -> '이지영' 이라는 값은 존재함.
print('성태호' in my_family.values())  # 결과값: False -> '성태호' 이라는 값은 존재 X.

# for 반복문 실행 하여 my_family 사전(dictionary)에 존재하는 값(value) 목록 하나씩 출력
for value in my_family.values():  # value - for 반복문에서 사용되는 변수
    # 수행 부분
    print(value)  # 반복 실행 명령

# my_family 사전(dictionary)에 어떤 키(key)들이 있는지 목록 출력
print(my_family.keys())

# '엄마' 이라는 값이 있는지 확인
print('엄마' in my_family.keys())  # 결과값: True -> '엄마' 이라는 값은 존재함.
print('삼촌' in my_family.keys())  # 결과값: False -> '삼촌' 이라는 값은 존재 X.

# for 반복문 실행 하여 my_family 사전(dictionary)에 존재하는 키(key) 목록 하나씩 출력
for key in my_family.keys():  # key - for 반복문에서 사용되는 변수
    # 수행 부분
    print(key)  # 반복 실행 명령

# for 반복문 실행 및 my_family.keys() 함수 사용하여
# my_family 사전(dictionary)에 존재하는 키(key), 값(value) 모든 쌍 하나씩 출력
for key in my_family.keys():  # key - for 반복문에서 사용되는 변수
    value = my_family[key]   # my_dictionary 사전에 저장된 값 가져와서 value 변수 저장
    # 수행 부분
    # print(key)  # 반복 실행 명령
    print(key, value)  # 반복 실행 명령 - key-value pair (키-값 쌍) 모두 출력

# for 반복문 실행 및 my_family.items()
# my_family 사전(dictionary)에 존재하는 키(key), 값(value) 모든 쌍 하나씩 출력
for key, value in my_family.items():  # key - for 반복문에서 사용되는 변수
    # 수행 부분
    # print(key)  # 반복 실행 명령
    print(key, value)  # 반복 실행 명령 - key-value pair (키-값 쌍) 모두 출력