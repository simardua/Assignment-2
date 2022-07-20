x = ["S001", "S002", "S003", "S004"] 
y = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
z = [85, 98, 89, 92]

result = [{x: {y: z}} for (x, y, z) in zip(x,y,z)]

print("Original strings:")
print(x)
print(y)
print(z)
print("\nNested dictionary:")
print(result)
