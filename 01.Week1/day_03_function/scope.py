age = 100  # global

def parent_func():  # enclosed
    age = 30

    def child_func(): # local
        age = 20
        print(age, 'child_func')

    child_func()
    print(age, 'parent_func')

parent_func()
print(age, 'global')