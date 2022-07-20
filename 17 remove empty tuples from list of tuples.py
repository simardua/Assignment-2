x = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print (x)
for i in x:
    if(len(i)==0):
        x.remove(i)
print (x)
