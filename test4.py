def to_decimal(input_str):
    decimal_digit = 0
    for  i in input_str:
        #a=0
        #decimal_digit =int(decimal_digit+ int(i*(2**(len(input_str)-1-a))))
        decimal_digit = decimal_digit*2 +int(i)
        #a+=1
    return decimal_digit
if __name__ == "__main__":
    input_str = "10011"
    print(to_decimal(input_str))

