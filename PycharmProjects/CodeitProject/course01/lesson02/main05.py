# 05. 칼로리 계산기
# 참고
# 컴파일 실행 후 콘솔(Console) 창 출력 메시지 의미
# Process finished with exit code 0
# 직역하면 종료 코드 0으로 프로그램이 종료되었다는 것인데,
# 보통 0 은 에러 없이 프로그램이 성공적으로 실행되었다는 것을 의미함.
# 그래서 위 메시지가 나오면 프로그램이 잘 실행되었다고 생각하면 된다.

# 파이썬 코드 스타일 가이드 라인 (PEP 8 – Style Guide for Python Code)
# 참고 URL - https://www.python.org/dev/peps/pep-0008

# 힌트 1 - 변수에 값을 저장하기 위해 필요한 기호는 =입니다.
# 힌트 2 - 변수에 값을 저장하려면 =의 왼쪽에는 변수 이름을, 오른쪽에는 저장하고자 하는 값을 적으면 됩니다.
# 실습 설명
# 변수를 배웠으니 한 번 사용해 봅시다.
# 총 다섯 가지 과자가 있습니다.
#
# kitkat: 190 칼로리
# oreos: 502 칼로리
# pringles: 292 칼로리
# twix: 135.9 칼로리
# cheetos: 485 칼로리
# 과자를 다양하게 조합해서 먹었을 때 총 몇 칼로리인지 계산해 보려고 하는데요. 각 과자의 이름을 변수 이름으로 사용하여, 해당 과자의 칼로리를 저장해 주세요.
#
# 변수를 사용하는 코드는 이미 작성되어 있으니, 여러분은 변수를 정의만 하면 됩니다. 변수를 제대로 정의하시면 콘솔에는 이렇게 출력이 됩니다.

# 출력 결과
# 1194
# 1940
# 929.9
# 1880

# 코드
# 여기에 코드를 작성하세요.
kitkat = 190
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485

# 다양한 과자 조합
# 파이썬 문자열 포맷팅
# 참고 URL - https://www.codeit.kr/learn/courses/intro-to-python-programming/2756
# f-string 예시
# price = 500
# print(f'The price is {price}won')
print(kitkat + oreos * 2, 'kcal', sep='')   # sep='' 사용해서 kitkat + oreos * 2 와 'kcal'사이에 있는 띄어쓰기 -> 공백 변경
print(cheetos * 4, 'kcal', sep='')   # sep='' 사용해서 cheetos * 4 와 'kcal'사이에 있는 띄어쓰기(' ') -> 공백('') 변경
print(pringles + oreos + twix, 'kcal')
print(pringles * 3 + oreos * 2, 'kcal')