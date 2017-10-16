operation = raw_input('Choose math operation (+, -, *, /): ')

x = int(raw_input("Enter the value for x: "))
y = int(raw_input("Enter the value for y: "))

if operation == '+':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '*':
    print(x * y)
elif operation == '/':
    print(x / y)
else:
    raise ValueError('Wrong operation!')

# print(x+y)
