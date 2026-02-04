# 03. 리스트 정렬

# 참고

# sorted 함수 - 정렬된 새로운 리스트 리턴
#              단, sorted 함수는 기존의 리스트를 전혀 건드리지 않고 원형 보존.
#              단지, 정렬된 새로운 리스트를 만들어서 리턴할 뿐이다.

# sort 함수 - 정렬된 리스트를 아무 것도 리턴 하지 않고 None 출력.
#            그 대신 기존 리스트 그 자체를 정렬한다. (리스트 원형 보존 X)

# 리스트를 정렬하기 위해서는 sorted 함수를 사용할 수 있고, sort 함수 사용할 수도 있다.
# 다만 이 두 함수는 살짝 다르다.
# sorted 함수는 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴한다. (리스트 원형 보존.)
# 반면 sort 함수는 정렬된 리스트를 아무 것도 리턴 하지 않고 None 출력하고 기존 리스트 그 자체를 정렬한다. (리스트 원형 보존 X)


# sorted 함수
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

new_list = sorted(numbers)   # 오름차순 정렬된 새로운 리스트 리턴 및 new_list 변수 저장
reverse_new_list = sorted(numbers, reverse=True)   # 내림차순(거꾸로) 정렬된 새로운 리스트 리턴 및 new_list 변수 저장 (reverse=True 반대로 정렬 의미)
print(new_list)  # 오름차순 정렬된 new_list 리스트 출력
print(reverse_new_list)  # 내림차순(거꾸로) 정렬된 reverse_new_list 리스트 출력
print(numbers)   # numbers 리스트 기존 그대로 출력

# sort 함수
# print(numbers.sort())  # 오름차순 정렬된 리스트를 아무 것도 리턴 하지 않고 None 출력.
# print(numbers.sort(reverse=True))  # 내림차순(거꾸로) 정렬된 리스트를 아무 것도 리턴 하지 않고 None 출력.
numbers.sort()  # numbers 리스트 자체 오름차순 정렬
print(numbers)

numbers.sort(reverse=True)  # numbers 리스트 자체 내림차순(거꾸로) 정렬
print(numbers)