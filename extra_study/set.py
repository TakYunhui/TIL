set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

def intersection(set_a, set_b):
    result = set()
    for element in set_a:
        if element in set_b:
            result.add(element)
    return result
        
print(intersection(set1, set2))



def diff(set_a, set_b):
    result = set()
    for element in set_a:
        if element not in set_b:
            result.add(element)
    return result

print(diff(set1, set2))


def u(set_a, set_b):
    result = set()
    for element in set_a:
        result.add(element)
    for element in set_b:
        result.add(element)

    return result

print(u(set1, set2))