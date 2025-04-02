a  = float(input("Enter the first number:"))
b  = float(input("Enter the second number:"))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

val = int(input("enter one of the 4 options:"))

def operation(val):
    match val:
        case 1 :
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            print(a / b)

operation(val)
