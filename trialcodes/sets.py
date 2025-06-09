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