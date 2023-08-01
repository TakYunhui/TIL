# make_new_dict(scores) -> {'Bob': 92, 'Charlie': 80, 'Eva': 85}
scores = {
    'Alice': 75,
    'Bob': 92,
    'Charlie': 80,
    'David': 60,
    'Eva': 85
}

def make_new_dict(scores):
    new_dict = {}
    for k, v in scores.items():
        if v >= 80:
            new_dict[k] = v
    return new_dict


print(make_new_dict(scores))