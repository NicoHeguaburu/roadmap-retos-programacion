for i in range(1,11):
    print(i)


n = 1

while n <= 10:
    print(n)
    n += 1


def count(x=1):
    if x <=10:
        print(x)
        x += 1
        count(x)


count()