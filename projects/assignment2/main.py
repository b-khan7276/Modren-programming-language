import module as mod



select = (input("Please select select operation  + - * /" ))
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your first number: "))

if select == "+":
    print(num1,"+", num2 ,"=", mod.add(num1, num2) )

elif select == "-":
        print(num1,"-", num2 ,"=", mod.subtract(num1, num2) )
elif select == "/":
        print(num1,"/", num2 ,"=", mod.divide(num1, num2) )
elif select == "*":  
        print(num1,"*", num2 ,"=", mod.multiply(num1, num2) )
else:
    print("Invalid input Please try again... shutting down ok !!!")