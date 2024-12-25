
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
op = str(input("Enter the opration. Enter 'ad' for addition, 'su' for subtraction, 'di' for division and 'mi' for multiplication:"))

if op == "ad":
    ans = n1+n2
if op == "su":
    ans = n1-n2
if op == "di":
    ans = n1/n2
if op == "mi":
    ans = n1*n2
print(f"The answer is {ans}")