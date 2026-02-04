# 프로그래밍과 데이터 in Python
# 2. for 반복문
# 01. for 반복문

# 참고
# for 반복문
# 상황에 따라 for문을 쓰는 게 while문을 쓰는 것보다 더 깔끔할 수 있다.
# 그런데 while 반복문과는 다르게 for 반복문에는 조건 부분이 없다.
# for문은 while문과는 조금 다르게 동작한다.


# for 반복문 사용 예시
my_list = [2, 3, 5, 7, 11]

# for 반복문 사용해서 my_list 리스트의 마지막 요소까지 계속 반복하다가 종료
for number in my_list:  # number - for 반복문에서 사용되는 변수
    # 수행 부분
    print(number)  # 반복 실행 명령

# while 반복문 사용 예시
my_list = [2, 3, 5, 7, 11]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

