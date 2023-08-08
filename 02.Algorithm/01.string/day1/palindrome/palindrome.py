t = int(input())
# 가로, 세로 회문 찾기
def detect_palindrome(word):
    if word == word[::-1]:
        print(word, word[::-1])
        return True
    return False

    # for 문에서 row_word, col_word 만들기
    # 가로 세로 단어들이 지정 길이 인지 확인
    # 회문인지 확인 후, 회문이면 저장 

for tc in range(1, t+1):
    n, m = map(int, input().split())
    texts = [list(input().split()) for _ in range(n)]
    # print(texts)
    result = ''

    print(f'{tc} {result}')