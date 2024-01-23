
operator  =  input("Enter an operator (* - + /): ")
num1 = int(input("Ente the 1st number"))
num2 = int(input("Ente the 2nd number"))

 
 
 
if operator == "+":
    result = num1 + num2
    print(round(result,3))
if operator == "-":
    result = num1 - num2
    print(round(result,3))
if operator == "/":
    result = num1 / num2
    print(round(result,3))
if operator == "*":
    result = num1 * num2
    print(round(result,3))
else:
    print(operator)