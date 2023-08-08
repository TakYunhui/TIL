# 라이브 - 이진 검색 
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end: # 탐색 구간이 존재, 원소가 한 개 이상
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False             # 검색 실패