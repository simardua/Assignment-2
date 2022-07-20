x = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
result = {}
print("Original list:")
print(x)
for k, v in x:
    result.setdefault(k, []).append(v)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(result)
