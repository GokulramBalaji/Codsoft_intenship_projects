while True:
     def add(a,b):
          print("The sum of tow numbers",a,"+",b,"=",a+b)
     def sub(a,b):
          print("The subraction of b from a is",a,"-",b,"=",a-b)
     def mult(a,b):
          print("The Product of tow numbers",a,"*",b,"=",a*b)
     def div(a,b):
          print("The Division a of b from a is",a,"/",b,"=",a/b)
     x=int(input("Enter the first number :"))
     y=int(input("Enter the second number :"))
     z=int(input("Enter the arithmetic operation \n1 for additon \n2 for subraction \n3 for multiplication \n4 for division :"))
     if z==1:
         add(x,y)
     elif z==2:
         sub(x,y)
     elif z==3:
         mult(x,y)
     elif z==4:
         div(x,y)
     else:
         print("Kindly  reverify the arithmetic operation you have entered /nThank you")
