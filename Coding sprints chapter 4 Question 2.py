num = int(input("Please enter a number"))
result = 0
while num > 10:
    rem = num % 10
    result = result + rem
    num = int(num/10)
print("Sum of all digits for ", num ," is = ", result)
