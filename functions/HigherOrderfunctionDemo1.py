
def toBeCalled():
    print("to be called....")

def demo(a):
    print(a) #100 ,ok False, tobecal
    a()

# demo(100)    
# demo("ok")
# demo(False)
demo(toBeCalled)
        