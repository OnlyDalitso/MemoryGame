#3) Similarily, like the above problem, find the average of the sum of all digits of a number

number = int(input('Please enter a number'))
total = 0
total_digits =  0

while number > 10:
    digit = number % 10
    total = total + digit
    number = number // 10
    total_digits += 1

print('The average of all digits for ', number,' is = ',(total/total_digits))
