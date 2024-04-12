def prime_number(range1, range2):
    ans = []
    for num in range(range1, range2+1):
        if isprime(num):
            ans.append(num)    
    print(ans)
def isprime(num):
    if num <=1:
        return False
    elif num <=3:
        return True
    elif num % 2 == 0 or num %3 == 0:
        return False
    
    elif num % 5 == 0 or num % 7 == 0:
        return False
    
    else:
        return True


if __name__ == "__main__":
    range1 = int(input("enter the lowest range: "))
    range2 = int(input("enter the upper range:"))
    res = prime_number(range1, range2)
    print(res)