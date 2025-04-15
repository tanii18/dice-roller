def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if x==0 or y==0:
        print("error")
    else:
         return x/y
     
while True:
     print("choose an operation")
     print("1.add")
     print("2.subtract")
     print("3.multiply")
     print("4.divide")

     choice= input("enter your choice")

     if choice in["1","2","3","4"]:
         num1=float(input("enter first num"))
         num2=float(input("enter second num"))
         if choice=="1":
             print(f"addition of {num1} and {num2} is,{add(num1,num2)}")
         if choice=="2":
             print(f"subtraction of {num1} and {num2} is,{subtract(num1,num2)}")
         if choice=="3":
             print(f"multiplication of {num1} and {num2} is,{multiply(num1,num2)}")
         if choice=="4":
             print(f"addition of {num1} and {num2} is,{divide(num1,num2)}")
else:
    print("error bye")
     
            

