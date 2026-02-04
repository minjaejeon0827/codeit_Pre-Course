# 05. 온도 단위 바꾸기

# 참고

# 실습 설명
# 화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.

# 섭씨와 화씨의 관계식은 다음과 같습니다:
# °C = (°F − 32) ∗ 5 / 9

# 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요.
# 이 함수는 파라미터로 화씨 온도 fahrenheit를 받고,
# 변환된 섭씨 온도를 리턴합니다.

# 실습 결과
# 화씨 온도 리스트: [40, 15, 32, 64, -4, 11]
# 섭씨 온도 리스트: [4.4, -9.4, 0.0, 17.8, -20.0, -11.7]

# 힌트 1 - 화씨 온도를 섭씨 온도로 변환해 주는 fahrenheit_to_celsius 함수를 제공해 드리겠습니다.
#         def fahrenheit_to_celsius(fahrenheit):
#             return (fahrenheit - 32) * 5 / 9

# 힌트 2 - temperature_list에는 화씨 온도가 저장되어 있는데요.
#         이 값들을 모두 섭씨 온도로 변환해야 합니다.

#         한 번에 다 하려고 하지 말고, 하나씩 차근차근 생각해 봅시다.
#         2번 인덱스의 원소를 섭씨 온도로 바꾸기 위해서는 뭘 해야 할까요?

#         이렇게 하면 됩니다.

#         temperature_list[2] = fahrenheit_to_celsius(temperature_list[2])
#         만약 변환된 섭씨 온도를 소수점 첫째 자리까지 반올림하고 싶다면 이렇게 하면 됩니다.

#         temperature_list[2] = round(fahrenheit_to_celsius(temperature_list[2]), 1)

# 힌트 3 - 힌트 2에서는 하나의 원소에 대해서만 변환을 했는데요.
#         모든 원소에 대해서 하려면 반복문을 사용하면 좋겠죠?
#         반복문은 인덱스 0부터 인덱스 len(temperature_list) - 1까지 돌면 됩니다.

# 실습 해설

# 해설
# 온도 변환 함수
# 화씨 온도를 섭씨 온도로 변환해 주는 fahrenheit_to_celsius 함수는 이렇게 작성할 수 있습니다.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 한 번 이 함수를 활용해 봅시다.
# temperature_list에는 화씨 온도가 저장되어 있는데요.
# 만약 2번 인덱스의 원소를 섭씨 온도로 바꾸고 싶다면 뭘 해야 할까요?

# 이렇게 하면 됩니다.

# temperature_list[2] = fahrenheit_to_celsius(temperature_list[2])
# 그리고 만약 변환된 섭씨 온도를 소수점 첫째 자리까지 반올림하고 싶다면 이렇게 하면 되겠죠.

# temperature_list[2] = round(fahrenheit_to_celsius(temperature_list[2]), 1)

# 리스트의 모든 요소 변환
# 이제 temperature_list의 모든 원소를 섭씨로 변환하겠습니다.
# 반복문을 사용해야겠죠?
# 인덱스 0부터 인덱스 len(temperature_list) - 1까지 반복을 해야 하는데요.

# i = 0
# while i < len(temperature_list):
#     # 인덱스 i에 있는 요소 변환
#     i += 1

# 이렇게 하면 되겠네요.
# 이제 temperature_list의 인덱스 i에 있는 요소를 화씨에서 섭씨로 변환하면 코드가 완성됩니다.

# 모범 답안
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력

# 코드
def fahrenheit_to_celsius(fahrenheit):
    """
    Description: 화씨 온도에서 섭씨 온도로 바꿔 주는 함수

    Parameters: fahrenheit - 화씨 온도

    Returns: (fahrenheit - 32) * 5 / 9 - 섭씨 온도
    """

    # 여기에 코드를 작성하세요
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요
centigrade_list = []
i = 0
while i < len(temperature_list):
    centigrade_list.append(round(fahrenheit_to_celsius(temperature_list[i]), 1))
    i += 1

print("섭씨 온도 리스트: {}".format(centigrade_list))  # 섭씨 온도 출력
# print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력
