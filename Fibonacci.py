# Program to display the Fibonacci sequence up to n-th term
terms = int(input("How many terms?"))
num1, num2 = 0, 1
count = 0 

# if there is 0 or negative number, then asks for valid input...
if terms == 0 :
    print('please enter a valid number!!')

# if there is only one term, return n1
elif terms == 1:
    print('Fibonacci sequence upto ' + str(terms) + ' terms :')
    print(num1)

# generate fibonacci sequence
else :
    print('Fibonacci sequence upto ' + str(terms) + ' terms :')
    while count < terms :
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1

