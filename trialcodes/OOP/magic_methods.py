# callable objects and __call__() method
class Callable:
    def __call__(self, *args, **kwds):
        print("__call__ method is called")

obj = Callable()
obj()

# iterable objects and iterators
numbers = [2,5,8] # iterable
iterator1 = iter(numbers) # iterator
print(next(iterator1)) # 2
print(next(iterator1)) # 5
print(next(iterator1)) # 8
# print(next(iterator1)) # error
# StopIteration

class Berik:
    def __init__(self, age):
        if age < 1000:
            raise ValueError("Impossible age for the ONE")
        self.age = age
    

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.age
    
# Berikbek = Berik(1000)
# for age in Berikbek:
#     print(f"The age is {Berikbek.age}") # infinite printing is expected result

# Berik_obj = Berik(10000)
# obj_iterator = Berik_obj.__iter__()
# while True:
#     age = obj_iterator.__next__()
#     print(f"The age is {age}") # infinite printing is expected output

class FiniteBerik:
    def __init__(self, age, max_count):
        if age < 1000:
            raise ValueError("Impossible age for the ONE")
        self.age = age
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count+=1
        return self.age
    
FiniteBerikbek = FiniteBerik(1000, 5)
for age in FiniteBerikbek:
    print(age)