# index 접근 
# 어디에? list, srt ... 순서가 있는 sequence 자료형
# 슬라이싱이란...?


#      0  1  2  3  4  5  
#      |  |  |  |  |  |  
list = [1, 2, 3, 4, 5]
print(list[1: 4: 1]) # [2, 3, 4]
print(list[1: 4: 2]) # [2, 4]
print(list[1: 4: 3]) # [2]
# 슬라이싱 쓸 때는 범위 벗어나도 오류 없이 잘 나오니까 주의하자.
# list[start: end: step]
# | start에 작성한 내용은 그 index 번호부터 시작,
# | end에 작성한 내용은 그 index-1 번째 까지 만 출력
# | step에 작서안 내용은 start부터 end까지 step 만큼 건너 뛰면서
    # range(start, end, step)
print(list[1: 100])


# None을 사용하는 이유
# 아래는 다 값이 있다
# 0, '', False, [], {}
# None: 값 자체가 존재하지 않음을 나타내기 위해 존재
print()
print(None)