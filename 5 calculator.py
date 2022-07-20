print ("Select the choice\n1. Add\n2. Sub\n3. Multiply\n4. Divide")
choice = int(input("Enter the choice:"))
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == 1:
    ans=A+B
elif choice == 2:
    ans = A-B
elif choice == 3:
    ans = A*B
elif choice == 4:
    ans = A/B
else:
    print("Invalid input")

print("the answer is", ans)
