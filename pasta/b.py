a = [5, 9, 10, -1, 14, 23, 6, 30]
b = 0
s = 0
while (b<len(a)):
    if a[b]%2==0:
        print(f"Número par: {a[b]}")
        s+=a[b]
        b+=1
    else:
        s+=0
        b+=1
print(s)