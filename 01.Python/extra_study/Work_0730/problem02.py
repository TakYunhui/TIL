def under_60(scores):
    pass
    # 여기에 코드를 작성합니다.
    count = 0
    for score in scores:
        if score < 60:
            count += 1
    return count


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 20, 60, 90, 70]
    print(under_60(scores)) # 2
    # 아래 부터 추가 예제 코드 작성 가능합니다.

help(list)
