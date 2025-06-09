curly_set = {"here", "there", "everywhere"}
print(type(curly_set))
functional_set = set(("function", "method", "procedure"))
print(type(functional_set))

emppty_set = set()
print(type(emppty_set))

empty_not_set = {}
print(type(empty_not_set))  # This is a dictionary, not a set

list_with_duplicates = [1, 2, 3, 1, 2, 3]
set_from_list = set(list_with_duplicates)
print(set_from_list)  # {1, 2, 3}, duplicates are removed

# Hashable objects
some_tuple = (1, 2, 3)
print(type(some_tuple))  # <class 'tuple'>
print(hash(some_tuple))  # Hashable, can be used in sets or as dictionary keys
some_list = [1, 2, 3]
try:
    print(hash(some_list))  # Raises TypeError, lists are not hashable
except TypeError as e:
    print(f"Error: {e}")
some_set = {1, 2, 3}
print(type(some_set))  # <class 'set'>
print(hash(frozenset(some_set)))  # frozensets are hashable, can be used in sets or as dictionary keys

# Set operations
set_a = {"a", "b", "h"}
set_b = {"m", "b", "k", "l"}
set_c = {"k", "l"}
set_d = {"k", "l", "b"}

union = set_a | set_b | set_c
print("Union:", union)  
union_method = set_a.union(set_b, set_c)
print("Union using method:", union_method)  

intersection = set_a & set_b & set_d
print("Intersection:", intersection)  
intersection_method = set_a.intersection(set_b, set_d)
print("Intersection using method:", intersection_method) 

difference = set_a - set_b - set_c
print("Difference:", difference)  
difference_method = set_a.difference(set_b, set_c)
print("Difference using method:", difference_method)  

# Set methods
s1 = {"a", "b", "c"}
s2 = {"a", "d", "h"}
s3 = {"n", "b", "d"}

s1.update(s2, s3)
print("Updated set s1:", s1)  # {'a', 'b', 'c', 'd', 'h', 'n'}

s4 = {"a", "d", "h"}
s4.add("x")
s1.remove("d")
print("Set after addition and removal:", s1)  # {'a', 'b', 'c', 'h', 'n', 'x'}

s4.clear()
print("Cleared set s4:", s4)  # set() - empty set