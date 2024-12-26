# Gather user inputs

n1= float(input("Enter first number"))
n2 = float(input("Enter second number"))


#implement operation choice
op=input("choose the operation(+, -, *, /, ^): ")

if op =='+':
    result =n1+n2
    
elif op=='-':
    result =n1-n2

elif op =='*':
    result= n1*n2
    
elif op == '/':
    result =n1/n2
    
elif op =='^':
    result = n1**n2
    
else:
    print("Invalid Input")

# Output the Result

print(f"The Result is {result}")


