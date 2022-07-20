n = int(input("Enter a number: "))
sum = 0
temp=n
while n > 0:
   dig= n%10
   sum = sum + (dig ** 3)
   n=n//10
if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")
