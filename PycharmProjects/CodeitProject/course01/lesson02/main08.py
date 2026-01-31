# 08. 파라미터
# 참고
# 컴파일 실행 후 콘솔(Console) 창 출력 메시지 의미
# Process finished with exit code 0
# 직역하면 종료 코드 0으로 프로그램이 종료되었다는 것인데,
# 보통 0 은 에러 없이 프로그램이 성공적으로 실행되었다는 것을 의미함.
# 그래서 위 메시지가 나오면 프로그램이 잘 실행되었다고 생각하면 된다.

# 파이썬 코드 스타일 가이드 라인 (PEP 8 – Style Guide for Python Code)
# 참고 URL - https://www.python.org/dev/peps/pep-0008

# 파라미터를 매개변수라고도 한다.
# 파라미터는 함수를 정의할 때 쓰게 되는 변수를 말하는 별칭이라고 생각하면 된다.

# 함수 매개변수와 인수
# 참고 URL - https://wikidocs.net/24#_4
# 참고 2 URL - https://www.codeit.kr/community/threads/10416
# 참고 3 URL - https://www.codeit.kr/community/threads/5998
# 참고 4 URL - https://mingrammer.com/understanding-the-asterisk-of-python/

def hello(name=""):   # def 기호 사용하여 구현한 함수 정의의 첫줄을 함수의 '헤더'라고 부른다.
    """
    Description: [테스트] 사용자 정의 함수

    Parameters: name - 이름 (초기값 공백("") 설정)

    Returns: None
    """

    # 해당 hello 함수는 아래 2 줄의 명령 저장 및 실행
    print("Hello!")
    if ("" != name): print(name)   # 변수 name에 저장된 값이 공백("")이 아닌 경우
    print("Welcome to Codeit!")

# hello 함수 2번 호출
hello("Chris")  # hello 함수 name 파라미터로 문자열 "Chris" 인자값 전달
hello("Michael")  # hello 함수 name 파라미터로 문자열 "Michael" 인자값 전달
hello("")  # hello 함수 name 파라미터로 공백("") 인자값 전달
hello()   # hello 함수 name 파라미터로 인자값 전달 안함.