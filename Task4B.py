my_tuple = (10, 'hello', 3.14, 'world')
print(my_tuple)
for i in my_tuple:
    print(i)
print(my_tuple[1:3])    
print(my_tuple[:-1])    

t2 = (5, 0.5)
t3 = my_tuple + t2
print(t3)
my_tuple_modified = my_tuple[:3] + ("PI",)
print(my_tuple_modified)
