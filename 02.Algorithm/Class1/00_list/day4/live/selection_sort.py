# 라이브 - 선택 정렬 설명
def selectionSort(a, N):
    for i in range(N):
        minIdx = i # 구간의 가장 앞이 제일 작다고 가정
        for j in range(i+1, N): # 자기 자신은 검사 안 해서 i + 1부터 마지막까지지
            if a[minIdx] > a[j]:
                minIdx = j       # 주어진 구간에서 최소 값 위치 찾기
        a[i], a[minIdx] = a[minIdx], a[i] # 최소 값 찾았으면 교환 작업 1회 