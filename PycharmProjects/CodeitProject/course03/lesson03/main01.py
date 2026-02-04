# 프로그래밍과 데이터 in Python
# 3. 사전
# 01. 사전

# 참고
# 사전 (dictionary) - 여러 값을 모아놓을 수 있는 자료형
# 사전 자료형 <class 'dict'> (dictionary 줄임말)
# 보통 사전에서는 단어와 뜻이 하나의 쌍을 이룬다.
# 마찬가지로 파이썬의 사전은 key와 value가 하나의 페어(pair) 즉, 하나의 쌍을 이룬다.
# key-value pair (키-값 쌍)
# 그리고 사전 (dictionary)은 리스트 (list)와 다르게 딱히 순서라는 개념은 없다.
# 또한 핵심적인 차이점은 리스트의 인덱스는 0, 1, 2, 3, 4 ... 과 같은 정숫값들이라면
# 사전 (dictionary)의 key-value는 반드시 정수형일 필요 없다. (key-value는 문자열로 작성할 수 있다.)

# 파이썬 사전 (dictionary) 자료형
# 참고 URL - https://wikidocs.net/16

# 파이썬 사전 (dictionary) 자료형 중괄호 {} 쓰임
# 참고 URL - https://stackoverflow.com/questions/9197324/what-is-the-meaning-of-curly-braces


# 리스트 (list)
my_list = [2, 3, 5, 7, 11, 13]
# 리스트에서 요소(값)을 받아오기 위해 리스트 범위 안에 있는 정숫값으로 '인덱싱(indexing)' 하기.
print(my_list[1])
print(my_list[3])

# 사전 (dictionary)
# key-value pair (키-값 쌍)
# 사전 (dictionary) 사용 예시
# key: int(정수형)
# value: int(정수형)
# 쉼표(,)를 써서 3개의 쌍 구분하도록 구현 (5: 25, 2: 4, 3: 9)
my_dictionary = {
    5: 25,  # key: 5, value: 25
    2: 4,  # key: 2, value: 4
    3: 9  # key: 3, value: 9
}
# my_dictionary 변수가 담고 있는 값은 사전 자료형('dict')이다.
print(type(my_dictionary))  # 결과값 - <class 'dict'>

# my_dictionary 사전에 저장된 값 출력
print(my_dictionary[3])  # 결과값: 9 -> key: 3, value: 9

# my_dictionary 사전에 새로운 key-value pair (키-값 쌍) 추가
my_dictionary[9] = 81  # key: 9, value: 81 key-value pair (키-값 쌍) 추가
print(my_dictionary)

# 사전 (dictionary) 사용 예시 2
# key-value pair (키-값 쌍)
# key: str(문자열)
# value: str(문자열)
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영',
}

# my_dictionary 사전에 저장된 값 출력
print(my_family['아빠'])  # 결과값: '이석진' -> key: '아빠', value: '이석진'