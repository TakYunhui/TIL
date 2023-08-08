# 선택 정렬
# 최솟값을 

def selection_sort(arr):
    # 배열 전체 길이 만큼 조사
    # i -> 순차적으로 증가하는 index
    for i in range(len(arr)):
        # 최솟값의 index
        # 뒤에 조사하는 대상이 내 위치보다 작을지 클지 모르므로
        # 일단 내 위치가 제일 작다고 가정하고 조사
        min_idx = i
        for j in range(i+1, len(arr)):
            # 현재까지 최솟값이 담겨 있다고 판단되는 위치의 값과
            # 새롭게 조사할 j번째 위치의 값을 크기 비교
            if arr[min_idx] > arr[j]:
                # 최솟값의 위치 index 정보를 j 번째로 변경
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



arr = [93, 19, 63, 72, 13, 8, 1, 41, 33]
N = len(arr)
selection_sort(arr)
print(arr)