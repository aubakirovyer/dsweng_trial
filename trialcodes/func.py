# passing functions to variables
def cube(x) -> int:
    return x** 3

print(cube(3))
second_cube = cube
print(second_cube(2))
print('\n')

# passing functions as arguments
def apply_func(func, *args) -> list[int]:
    results = []
    for arg in args:
        results.append(func(arg))
    return results

print(apply_func(cube, 1,2,3,4,5))
print('\n')

# storing functions in data structures
def increment(x) -> int:
    return x + 1
def decrement(x) -> int:
    return x - 1

func_mapping = {
    'cube': cube,
    'increment': increment,
    'decrement': decrement
}
print(func_mapping['cube'])
print(func_mapping['cube'](2))
print(func_mapping['increment'])
print(func_mapping['increment'](2))
print(func_mapping['decrement'])
print(func_mapping['decrement'](2))

print('\n')

# return functions from other functions
def make_multiplier(factor: int):
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier
double = make_multiplier(2)
print(double(5))  # Output: 10
print("\n")

# all() - return False only if any elements of the iterable are false
print(all({}))
print(all([True, True, 10]))
print(all([True, 0]))
print(all([1, tuple(), [2, 'name']]))
print('\n')

# any() - return True only if any elements of the iterable are true
print(any({}))
print(any([True, True, 10]))
print(any([True, 0]))
print(any([1, tuple(), [2, 'name']]))
print('\n')



