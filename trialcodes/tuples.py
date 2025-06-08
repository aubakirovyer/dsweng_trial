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