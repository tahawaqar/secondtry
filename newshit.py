choice = int(input("Choose 1 for addition. Choose 2 for Subtraction.Choose 3 for Multiplication. Choose 4 for Division"))
num1 = int(input("Enter first num")) 
num2= int(input("Enter second num"))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)    