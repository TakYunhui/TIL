def make_odd_even(input_list):
    new_list = []
    for number in input_list:
        if number % 2 != 0:
            new_list.append(number * 3)
        else:
            new_list.append(number ** 2)
    return new_list

print(make_odd_even([1, 2, 3, 4, 5]))


    