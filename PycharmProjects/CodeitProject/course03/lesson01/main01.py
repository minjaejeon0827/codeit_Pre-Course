# 프로그래밍과 데이터 in Python
# 1. 리스트
# 01. 리스트

# 참고
# 리스트 (list) - 변수에 값을 여러 개 저장 하고 싶을때 사용
# 리스트 (list)의 요소 - 리스트 (list)에 존재하는 하나하나의 값 의미
# 리스트 (list)의 요소의 위치를 '인덱스(index)'라고 한다.
# 이 때, '인덱스(index)'를 통해 요소를 받아 오는 걸 '인덱싱(indexing)'이라고 한다.
# 파이썬에서 '인덱스(index)'는 1부터 시작하는게 아니라 0부터 시작한다.
# 파이썬에서 '마이너스(-) 인덱스(index)'도 존재한다.
# 예를들어
# 인덱스 -1에는 리스트 변수의 마지막 요소의 위치 의미
# 인덱스 -2에는 리스트 변수의 마지막 요소의 바로 왼쪽 위치 의미 (리스트 변수 오른쪽 끝에서 두 번째 값 의미)

# 리스트 슬라이싱(list slicing) - '인덱스(index)'를 통해 리스트 (list)의 요소를 하나씩 받아 오는게 아니라 아예 리스트의 일부를 통째로 잘라서 사용하는 방법이다.

my_num = 7  # 정수형
my_str = "Hello!"  # 문자열
my_bool = True  # 불린(Boolean)

# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13]  # numbers 리스트 - 정수형 값 2, 3, 5, 7, 11, 13 갖고 있는 리스트 변수 / '인덱스(index)' 0부터 5까지 존재. / '마이너스(-) 인덱스(index)' -1부터 -6까지 존재.
names = ["윤수", "혜린", "태호", "영훈"]  # names 리스트 - 문자열 값 "윤수", "혜린", "태호", "영훈" 갖고 있는 리스트 변수 / '인덱스(index)' 0부터 3까지 존재.  / '마이너스(-) 인덱스(index)' -1부터 -4까지 존재.

# 콘솔창(console) 리스트 출력
print(numbers)
print(names)

# 인덱싱 (indexing)
print(names[0])
print(names[1])

# '마이너스(-) 인덱스(index)'
print(numbers[-1])  # 리스트 변수의 마지막 요소 "13" 출력
print(numbers[-2])  # 리스트 변수의 마지막 요소의 바로 왼쪽 위치 의미 (리스트 변수 오른쪽 끝에서 두 번째 값 의미) "11" 출력
print(numbers[-6])  # 리스트 변수 왼쪽 맨 앞에 있는 값 의미) "2" 출력

# 오류 메시지 - "IndexError: list index out of range"
# 오류 의미 - '인덱스(index)'가 범위를 벗어났다는 의미이다.
# print(numbers[-7])  # '마이너스(-) 인덱스(index)' -1부터 -6까지 존재하는데, '인덱스(index)' -7 입력시 범위를 벗어나서 오류 발생.

print(numbers[1] + numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

# 오류 메시지 - "IndexError: list index out of range"
# 오류 의미 - '인덱스(index)'가 범위를 벗어났다는 의미이다.
# print(numbers[6])   # '인덱스(index)' 0부터 5까지 존재하는데, '인덱스(index)' 6 입력시 범위를 벗어나서 오류 발생.

# 리스트 슬라이싱(list slicing)
print(numbers[0:4])  # 인덱스 0부터 3까지 numbers 리스트의 일부를 통째로 잘라서 부분 리스트 만들기
print(numbers[2:])  # 인덱스 2부터 리스트의 마지막 요소 까지 numbers 리스트의 일부를 통째로 잘라서 부분 리스트 만들기
print(numbers[:3])  # 인덱스 0부터 인덱스 2까지 요소가 들어간 numbers 리스트의 일부를 통째로 잘라서 부분 리스트 만들기
new_list = numbers[:3]  # [2, 3, 5]
print(new_list[2])   # new_list 리스트 인덱스 2 요소 "5" 출력

# 리스트 요소 값 바꾸기
# numbers[0] = 7  # 지정 연산자(=)의 오른쪽에 있는 정수 값 7을 numbers 리스트 인덱스 0의 요소로 저장하기
# print(numbers)

numbers[0] = numbers[0] + numbers[1]  # 지정 연산자(=)의 오른쪽에 있는 numbers 리스트 0번 인덱스 요소 "2"와 1번 인덱스 요소 "3"를 더한 값을 numbers 리스트 인덱스 0의 요소로 저장하기
print(numbers)  # numbers 리스트 0번 인덱스 요소 "5" 출력
