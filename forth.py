tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

for i in range(len(tuple1)):
    if num(tuple1[i], list) or num(tuple1[i], tuple):
        for i in tuple1[i]:
            if i == 20:
                print(i)
