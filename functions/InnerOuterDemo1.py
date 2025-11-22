# def outer():
#     print("outer function called..")
#     def inner(x):
#         print("inner function called...",x)
#     inner(100)

# outer()        
        
        

def outer(x):
    def inner(a,b):
        return a + b
    return inner

x = outer(10)
print(x)
ans = x(100,200)
print("ans = ",ans)


        