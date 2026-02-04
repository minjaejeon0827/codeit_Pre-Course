# 프로그래밍 시작하기 in Python
# 2. 프로그래밍 기본 개념
# 04. 변수

# 변수란 데이터를 어떤 공간에 담아서 이름표를 붙여 주는 것이다.
# 대입 연산자(=) 오른쪽에 있는 값(4990)을 대입 연산자(=) 왼쪽 변수(burger_price)에 저장
burger_price = 4750   # burger_price 선언 및 4750 이라는 데이터를 burger_price 변수에 저장
fries_price = 1490   # fries_price 선언 및 1490 이라는 데이터를 fries_price 변수에 저장
drink_price = 1250   # drink_price 선언 및 1250 이라는 데이터를 drink_price 변수에 저장

print(burger_price)   # 버거(Burger) 1개 가격 출력
print(burger_price * 2)   # 버거(Burger) 2개 가격 출력
print(burger_price + fries_price)   # 버거(Burger) 1개 + 감자튀김 1개 가격 출력
print(burger_price * 3 + fries_price * 2 + drink_price * 5)   # 버거(Burger) 3개 + 감자튀김 2개 + 음료 5잔 가격 출력

# 아래의 코드 4줄은 가격을 전부 외우기고 어렵고 만약 가격이 바뀔 경우 유지보수 하기에 좋은 코드가 아니므로 변수 활용해서 코드 수정 필수!
# print(4990)   # 버거(Burger) 1개 가격 출력
# print(4990 * 2)   # 버거(Burger) 2개 가격 출력
# print(4990 + 1490)   # 버거(Burger) 1개 + 감자튀김 1개 가격 출력
# print(4990 * 3 + 1490 * 2 + 1250 * 5)   # 버거(Burger) 3개 + 감자튀김 2개 + 음료 5잔 가격 출력