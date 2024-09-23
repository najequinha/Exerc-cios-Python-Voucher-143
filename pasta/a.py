a = [5, 9, 10, -1, 14, 23, 6, 30]
b = 0
for i in a:
    if i % 2 == 0:
        b+= i
        print(f"Número par: {i}")
    else:
        b+=0
print(b)