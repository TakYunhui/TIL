temp = 0
min_index = 0
a = [4, 2, 3, 5, 1]

for i in range(0, 4):
    min_index = i

    for j in range(i+1, 5):
        if a[j] < a[min_index]:
            min_index = j

    temp = a[min_index]
    a[min_index] = a[i]
    a[i] = temp

print(a)