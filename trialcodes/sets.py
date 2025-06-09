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