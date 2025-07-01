variable = 'some value'
print(globals(), "\n")

def sum(x, y):
    res = x+y
    print(locals())
    return res

sum(5, 6)

# we can not only refer to global variable, but also create it
def square():
    global z
    z = 10
    return z**2

print(square())
print(z)

# however we cannot create a nonlocal variable
# def first():
#     def second():
#         nonlocal fi 
#         fi = 'bar'
#         print(fi)
#     second()
#     print(fi)