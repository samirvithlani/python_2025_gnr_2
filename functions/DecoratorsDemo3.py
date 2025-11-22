

def getAccess(func):
    
    def inner(**kwargs):
        if kwargs["role"]=="admin":
            func(**kwargs)
        else:
            print("not allowd...")    
    return inner        



@getAccess
def getData(**kwargs):
    print("accessing data",kwargs)
    
    
getData(name="amit",role="user")    