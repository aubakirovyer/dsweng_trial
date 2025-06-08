integer_tuple = (1)
print(type(integer_tuple))

empty_tuple = ()
print(type(empty_tuple))

string_tuple = ("here")
print(type(string_tuple))

# Tuple unpacking
some_tuple = (1, 2, 3)
print(some_tuple)
print(*some_tuple)

(a,b,c) = some_tuple
print(a,b,c)

# Comparison of tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)  # True, because they are equal
print(id(tuple1), id(tuple2)) 

# Immutable objects that are equal have different ids
x = 2 ** 1000
y = 2 ** 1000
print("\n")
#print(x, y)
print(x == y)  # True, because they are equal
print(id(x), id(y))  # Different ids, because they are immutable objects
print(x is y)  # False, because they are different objects

x = (1, 2, "python" * 1000)
y = (1, 2, "python" * 1000)
print("\n")
#print(x, y)
print(x == y)  # True, because they are equal
print(id(x), id(y))  # Different ids, because they are immutable objects
print(x is y)  # False, because they are different objects