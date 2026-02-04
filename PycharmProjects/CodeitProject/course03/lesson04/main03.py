# 프로그래밍과 데이터 in Python
# 4. 파이썬 데이터의 비밀
# 03. 리스트와 문자열

# 참고
# 리스트(list)는 문자열(str)과 굉장히 유사한 구조를 가지고 있다.
# 리스트(list)는 어떤 자료형을 나열한 거라면 문자열(str)은 문자를 나열한 거라고 볼 수 있다.
# 문자열(str)도 리스트(list)처럼 인덱스 0부터 시작한다.
# 파이썬에서 리스트(list)와 문자열(str)이 어떻게 비슷하고 어떻게 다른지 확인해 보자.
# 리스트(list)와 문자열(str)이 인덱싱(indexing)과 슬라이싱(slicing)이 가능한 이유는
# 리스트(list)와 문자열(str)이 구조적으로 비슷하기 때문이다.
# 반면 문자열(str)과 리스트(list)의 차이점도 존재한다.
# 문자열(str)은 리스트(list)와 달리 요소(값) 수정이 불가하다.
# 리스트(list)는 수정해도 되지만 문자열(str)은 요소(값) 수정할 수 없다.
# 단, 문자열(str)은 요소(값) 수정이 불가하지만 문자열(str) 연결(Concatenating)은 가능하다.
# 문자열(str) 연결(Concatenating) 예시는 아래와 같다.
# name = 'codeit' + 'it'
# 위의 코드 처럼 문자열(str)을 수정한게 아니라 이 2가지 문자열(str)을 이용해서 새로운 문자열(str)을 만들었을 뿐이다.
# 문자열(str)을 수정하지 않았기 때문에 오류가 발생하지 않는 것이다.

# ***** 문자열(str)과 리스트(list)의 비슷한 점 *****

# 리스트(list) 인덱싱(indexing)
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0])  # alphabet_list 리스트 0 인덱스 자리에 있는 요소(값) 문자열 'A' 출력
print(alphabet_list[1])  # alphabet_list 리스트 1 인덱스 자리에 있는 요소(값) 문자열 'B' 출력
print(alphabet_list[4])  # alphabet_list 리스트 4 인덱스 자리에 있는 요소(값) 문자열 'E' 출력
print(alphabet_list[-1]) # alphabet_list 리스트 -1 인덱스 자리에 있는 요소(값) 문자열 'J' 출력

# 문자열(str) 인덱싱(indexing)
alphabet_string = 'ABCDEFGHIJ'
print(alphabet_string[0])  # alphabet_string 문자열 변수 0 인덱스 자리에 있는 요소(값) 문자열 'A' 출력
print(alphabet_string[1])  # alphabet_string 문자열 변수 인덱스 자리에 있는 요소(값) 문자열 'B' 출력
print(alphabet_string[4])  # alphabet_string 문자열 변수 인덱스 자리에 있는 요소(값) 문자열 'E' 출력
print(alphabet_string[-1]) # alphabet_string 문자열 변수 -1 인덱스 자리에 있는 요소(값) 문자열 'J' 출력

# 리스트(list) 슬라이싱(slicing)
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0:5])  # 인덱스 0부터 4까지 alphabet_list 리스트의 일부를 통째로 잘라서 부분 리스트 만들기
print(alphabet_list[4:])  # 인덱스 4부터 리스트의 마지막 요소 까지 alphabet_list 리스트의 일부를 통째로 잘라서 부분 리스트 만들기
print(alphabet_list[:4])  # 인덱스 0부터 인덱스 3까지 요소가 들어간 alphabet_list 리스트의 일부를 통째로 잘라서 부분 리스트 만들기

# 문자열(str) 슬라이싱(slicing)
alphabet_string = 'ABCDEFGHIJ'
print(alphabet_string[0:5])  # 인덱스 0부터 4까지 alphabet_string 문자열 변수의 일부를 통째로 잘라서 부분 문자열 만들기
print(alphabet_string[4:])  # 인덱스 4부터 문자열 마지막 요소 까지 alphabet_string 문자열 변수의 일부를 통째로 잘라서 부분 문자열 만들기
print(alphabet_string[:4])  # 인덱스 0부터 인덱스 3까지 요소가 들어간 alphabet_string 문자열 변수의 일부를 통째로 잘라서 부분 문자열 만들기

# 문자열(str) 연결(Concatenating)
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2  # str_1 문자열 변수와 str_2 문자열 변수 연결
print(str_3)

name = 'codeit' + 'it'
print(name)

# 리스트(list) 연결(Concatenating)
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2  # list_1 리스트와 list_2 리스트 연결
print(list_3)

# 리스트(list) len 함수 - 리스트에 몇 개의 요소(값) 있는지 확인
my_list = [2, 3, 5, 7, 11]
print(len(my_list))

# 문자열(str) len 함수 - 문자열의 길이 확인 (' ' 띄어쓰기, 느낌표(!) 또한 문자열의 길이 포함)
my_string = 'Hello world!'
print(len(my_string))

# ***** 문자열(str)과 리스트(list)의 차이점 *****

# 리스트(list) 요소(값) 바꾸기 가능(Mutable)
numbers = [1, 2, 3, 4]
numbers[0] = 5   # numbers 리스트 0 인덱스 요소(값) 5로 바꾸기
print(numbers)

# 문자열(str) 요소(값) 바꾸기 불가(Immutable)
name = 'codeit'
# 아래 코드 실행시 오류 메시지 출력
# 오류 메시지 - "TypeError: 'str' object does not support item assignment"
# 오류 사유 - 문자열(str)은 리스트(list)와 달리 요소(값) 수정이 불가하다.
name[0] = 'C'
print(name)

