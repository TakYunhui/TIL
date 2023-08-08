import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

# char: target의 값이 내 pattern 안에 몇번째에 있는지 조사
    def search(pattern, char):
        # 어디까지 동일한 값을 가지는지 확인
        for i in range(len(pattern)-2, -1, -1):
            # 동일한 값이 있다면
