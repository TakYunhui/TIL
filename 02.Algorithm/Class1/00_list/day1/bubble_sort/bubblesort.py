def bubble_sort(numbers):
    # n-1 번째까지 조사를 해나갈 것.
    # 조사할 범위를 i에 지정
    # 0번과 1번을 비교했다면 0번부터 다시 조사할 필요 x
    # 우리의 목적은 정렬!!
    # range(start, end, step)
    # start: 작성된 정수부터 시작
    # end: 작성된 정수 + step 까지 
    # step: 다음 정수의 값
    for i in range(len(numbers) - 1, 0, -1):
        # print(i) # 4 3 2 1
        # 이번 회차에 조사할 범위 i
        # j번과 j+1까지 조사
        for j in range(i):
            # print(numbers[j]) # 55 7 78 12 / 55 7 78 / 55 7 / 7
            # j가 다음 위치 보다 값이 크면 (오름차순 기준)
            if numbers[j] > numbers[j+1]:
                # 둘의 값을 바꿔치기 한다.
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
                # 파이썬 할당
                # numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                # 바꿔치기 되는 수, 변하는 과정 확인
                # print(numbers, numbers[j], numbers[j+1])
    return  numbers


                


numbers = [55, 7, 78, 12, 43]
print(bubble_sort(numbers))

# 내림차순 정렬해보기