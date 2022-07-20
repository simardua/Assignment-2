print ("1. cude\n2. sphere\n3. cylinder")
a=int(input("Enter the choice: "))
if a == 1:
    s=float(input("Enter side of cude: "))
    print(6*(s**3))
elif a == 2:
    r= float(input("Enter radius of sphere: "))
    print(2*3.14*(r**2))
elif a == 3:
    r1=float(input("Enter the radius of cylinder: "))
    h=float(input("Enter height of cylinder: "))
    print(2*3.14*(r1+h))
else:
    print("Enter the correct choice")
    
