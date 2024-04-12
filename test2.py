def fib(n):
    lst = []
    for i in range(n):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        elif i>=2:
            lst.insert(i, lst[i-1]+lst[i-2])
    print(lst)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    fib(n)
        