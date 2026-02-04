# 프로그래밍 핵심 개념 in Python
# 1. 자료형
# 15. 자료형 퀴즈 II

# 질문 1 30 XP
# 다음 중 코드의 실행 결과가 True인 것을 모두 고르세요.
# 정답: print((12 >= 10 and not 3 > 4) or 3 ** 2 != 9) / print(True and (True or False)) / print(False == False)
# 해설:
# 1. 부등호 왼쪽의 int(2.5) + int(3.8)은 2 + 3과 같기 때문에 5입니다. 부등호 오른쪽의 int(str(1) + str(2))는 int("1" + "2")와 같고, 이는 int("12")와 같기 때문에 12입니다. 5 > 12는 거짓이기 때문에 False가 나옵니다.
# 2. 12 >= 10는 True이고, not 3 > 4는 not False이기 때문에 True입니다. 따라서 괄호 안의 값은 True and True로 True입니다. 3 ** 2은 9가 맞기 때문에, 3 ** 2 != 9라는 수식은 False입니다. True or False의 결괏값으로 True가 나옵니다.
# 3. 오른쪽 괄호 안의 True or False의 값은 True입니다. 괄호 밖과 연산하면 True and True이기 때문에 True가 나옵니다.
# 4. 오른쪽 괄호 안의 True and False의 값은 False입니다. 괄호 밖과 연산하면 not True or False, 즉 False or False이기 때문에 False가 나옵니다.
# 5. False는 False와 같기 때문에 False == False는 True입니다.
# 따라서 2, 3, 5번이 정답입니다.

print(int(2.5) + int(3.8) > int(str(1) + str(2)))
print((12 >= 10 and not 3 > 4) or 3 ** 2 != 9)
print(True and (True or False))
print(not True or (True and False))
print(False == False)

# 질문 2 30 XP
# 다음 중 코드의 실행 결과가 잘못된 내용을 모두 고르세요.
# 정답:
# print(type(4 / 2))
# <class 'int'>
# print(type("True"))
# <class 'bool'>
# print(type(2 * 3 == 6))
# <class 'int'>

# 해설:
# 1. 4 / 2는 2.0입니다. 따라서 <class 'int'>가 아니라 <class 'float'>가 출력됩니다.
# 2. "True"는 문자열입니다. 따옴표가 없는 True가 불린이죠. 따라서 <class 'bool'>이 아니라 <class 'str'>이 출력됩니다.
# 3. 10 <= 7은 결괏값이 불린 False입니다. 옳은 보기입니다.
# 4. 2 ** 3은 정수형 8이지만 2.0 ** 3은 소수형 8.0입니다. 옳은 보기입니다.
# 5. 2 * 3 == 6은 결괏값이 불린 True입니다. 따라서 <class 'int'>가 아니라 <class 'bool'>이 출력됩니다.
# 1, 2, 5번이 잘못되었습니다.

print(type(4 / 2))
# <class 'int'>

print(type("True"))
# <class 'bool'>

print(type(10 <= 7))
# <class 'bool'>

print(type(2.0 ** 3))
# <class 'float'>

print(type(2 * 3 == 6))
# <class 'int'>