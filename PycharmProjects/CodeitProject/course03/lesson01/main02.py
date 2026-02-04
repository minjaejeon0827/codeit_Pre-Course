# 02. 리스트 함수

# 참고
# 리스트에 사용할 수 있는 함수
# len 함수 - 리스트의 요소가 몇개인지(길이가 몇인지) 리턴 (길이 - length 줄임말)
# append 함수 - 리스트의 가장 오른쪽에 새로운 요소(값) 추가 ('추가 연산'이라 부른다.)
# del 함수 - 리스트의 특정 '인덱스(index)' 요소(값) 제거 (삭제 - delete 줄임말)
#           그리고 삭제된 요소의 오른쪽에 있던 값들은 모두 하나씩 앞으로 당겨진다. (기존) 인덱스 -> (변경) 인덱스 - 1
# insert 함수 - 리스트의 특정 '인덱스(index)' 요소(값) 삽입(추가) ('삽입 연산'이라 부른다.)
# 참고 URL - https://stackoverflow.com/questions/53932704/why-doesnt-list-insert-with-negative-index-insert-the-item-at-the-end

# 파이썬 append 함수, extend() 함수 차이
# 참고 URL - https://www.geeksforgeeks.org/python/append-extend-python/

# 파이썬 del 함수, remove(), pop() 함수 차이
# 참고 URL - https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists#:~:text=and%20pop%20removes%20the%20item%20at%20a%20specific%20index%20and%20returns%20it.&text=Use%20del%20to%20remove%20an,value%20occurs%20in%20the%20list.

numbers = []  # 요소가 없고 비어있는 numbers 리스트

# len 함수
print(len(numbers))  # 해당 numbers 리스트의 요소가 몇개인지(길이가 몇인지) 출력

# append 함수
numbers.append(5)  # numbers 리스트 가장 오른쪽에 새로운 요소 "5" 추가
numbers.append(8)  # numbers 리스트 가장 오른쪽에 새로운 요소 "8" 추가
print(numbers)
print(len(numbers))  # 해당 numbers 리스트의 요소가 몇개인지(길이가 몇인지) 출력

# del 함수
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# del numbers[3]  # numbers 리스트 인덱스 3 요소 "7" 삭제
print(numbers)

# insert 함수
numbers.insert(4, 37)  # numbers 리스트 인덱스 4 요소 "37" 삽입(추가)
print(numbers)