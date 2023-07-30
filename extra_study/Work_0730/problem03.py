def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    for key in user_data.keys():
        if user_data[key] == '':
            return False
    return True


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    user_data3 = {
        'id': '',
        'password': '',
    }
    print(is_user_data_valid(user_data3)) 
    # False 

    user_data4 = {
        'id': 'jungssafy',
        'password': '',
    }
    print(is_user_data_valid(user_data4)) 
    # False
