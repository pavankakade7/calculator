def addition(num1,num2):
    result=num1+num2
    print("{0} + {1} ={2}".format(num1,num2,result))
def subtraction(num1,num2):
    result=num1-num2
    print("{0} - {1} ={2}".format(num1,num2,result))
def multiplication(num1,num2):
    result=num1*num2
    print("{0} * {1} ={2}".format(num1,num2,result))
def division(num1,num2):
    if num2==0.0:
        print("we can not do division becoz we can not divide any number by zero")
    else:
        result=num1/num2
        print("{0} / {1} ={2}".format(num1,num2,result))




while True:
    print("what do you want to do?")
    print("1 Addition")
    print("2 subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("If you want to quit press Q ")
    

    choice=input("Enter your choice : ")

   

    num1=float(input("enter the number 1 : "))
    num2=float(input("enter the number 2 : "))

    if(choice=='q'or choice=='Q'):
        break
    elif(choice=='1'):
        addition (num1,num2)
    elif(choice=='2'):
        subtraction (num1,num2)
    elif(choice=='3'):
        multiplication(num1,num2)
    elif(choice=='4'):
        division(num1,num2)
    else:
        print("Invalid input")
    

    
