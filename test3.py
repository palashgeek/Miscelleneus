def happy_number(n):
    lst = []
    while n!=1:
        if n in lst:
            return False
        else: 
            lst.append(n)
            n = sum(int(i)**2 for i in str(n))  
            print(lst)
            print(n)
    else:
        return True
    
n = input("Enter a number:")
if happy_number(n):
    print("Happy")
else:
    print("not happy")
'''def happy_number(n):
	if n>1:
		m = 0
		m = n%10*n%10
		n = n//10
		m+= n*n
		happy_number(m)
	elif n==1:
		return True
	else:
		return False
	
n = 82
happy_number(n)'''

