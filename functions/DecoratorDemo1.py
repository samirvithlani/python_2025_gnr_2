
#decorators
def order_food(func): #3 func == throw_party
    
    def inner(): #6
        print("ordering food..") #7
        func() #throw_party
    
    return inner #4   


@order_food #2 #5
def throw_party():
    print("throwing party..")


throw_party() #1    