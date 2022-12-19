
a = 15

def f(l):
    l.append(2)
    print(l)
    print(a)

l = []
l.append(1)
f(l[:])
print(l)

