def getUsers(*args):
    return [i.upper() for i in args]

print(getUsers("ram","shyam","ram"))


#return unique list

#apply 10 %
def getDiscount(*args):
    return [i*0.9 for i in args if (isinstance(i,int)and not isinstance(i,bool))]

print(getDiscount(10,20,30,44,50,True,"java","amit",100))
#[9,18,27...]

# def getData(**kwargs):
#     pass


# getData(name="ram",age=22,active=False,city="Ahmedabad",country="India",salary=34500)
#{'int':[age,salary],'str':[name,city,country]...}

no = 10
print(type(no).__name__)