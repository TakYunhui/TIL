try:
    num = int(input('100으로 나눌 값을 입력해: '))
    print(100/num)
except (ValueError, ZeroDivisionError):
    print('제대로 넣어')
# except ZeroDivisionError:
#     print('0 안 됨')
except:
    print('에러임')