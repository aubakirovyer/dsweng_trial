def coffee(variety = '100% Arabica'):
    print(variety, '\n')

def milk(func):
    def wrapper():
        print('hot milk')
        func()
    return wrapper

def sugar(func):
    def wrapper():
        print('no sugar')
        func()
    return wrapper

@milk
@sugar
def coffee_2(variety = '100% Arabica'):
    print(variety, '\n')

order = milk(sugar(coffee))
order()

coffee_2()

def count_guests(func):
    count = 0
    def wrapper(func_arg: str):
        nonlocal count
        count+=1
        func(func_arg)
        print(f"The number of guests arrived: {count}")
    return wrapper

@count_guests
def greet_the_guest(guest_name: str):
    print(f"We greet you, Dear {guest_name}")

greet_the_guest("Finn Arth")
greet_the_guest("Qasiret Abdildin")
greet_the_guest("Yernur Aubakirov")

