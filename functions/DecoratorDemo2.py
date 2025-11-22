def safeDiv(func):
    
    def inner(x,y):
        print("inner called..")
        if(y==0):
            print("can not divide by zero")
        else:    
            func(x,y)

    return inner

@safeDiv
def div(no1,no2):
    print(no1/no2)


div(10,0)    