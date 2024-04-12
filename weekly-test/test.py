'''0 to 100 its free == 0rs
101 to 200 == 10rs/pu
201 to 350 == 15rs/pu
above 350 >20rs/pu
'''
'''input units from user then return the bill amount '''

def bill_amount():
    n = int(input("Enter your electricity Units Used This Month:"))
    bill = 0
    if n <= 100:
        return f"the electricity bill for this month is {0} rupees"
    elif 100<n<=200:
        return   f"the electricity bill for this month is {10*(n-100)} rupees"
    elif  200<n<=350:
        return  f"the electricity bill for this month is {10*100 + 15*(n-200)} rupees"
    elif n>350:
         return  f"the electricity bill for this month is {10*100 + 15*150 + 20*(n-350)} rupees"


print(bill_amount())        
        
