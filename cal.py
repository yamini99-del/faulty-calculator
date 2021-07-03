print("********faulty calculator********")
i=1
while(i>0):
    print("select the operator + ,-,/,*")
    ope=input()
    num1=int(input("enter a first number : "))
    num2=int(input("enter a second number: "))
    if(ope=='*'):
       if(num1==45 and num2==3):
           print("555")
       else:    
         mult=num1*num2
         print(mult)
    elif(ope=="+"):
        if(num1==56 and num2==9):
           print("77")
        else:    
          add=num1+num2
          print(add)
    elif(ope=='/'):
        if(num1==56 and num2==4):
            print("6")
        else:
          div=num1/num2
          print(div)
    elif(ope=='-'):
       sub=num1-num2
       print(sub)
    else:
       print("unexpected error")
    i=int(input("to exit enter 0 or press any other num to continue"))   

