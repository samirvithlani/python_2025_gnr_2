#open("demo1.txt") ->mode r
# file = open("demo1.txt","a")
# file.write("this is first file using write()")
# file.close()


# with open("files/demo1.txt","a") as f:
#     print("this is using print()",file=f)



data = ["amit","sumit","raj","jay","ajay"]
data = [f"\n{i}" for i in data]

with open("demo2.txt","a") as file:
    file.writelines(data)

users = {"name":"amit","age":23,"city":"Ahmedabad","salary":23000}    
file2 = open("users.txt","a")
for i,j in users.items():
    file2.write(f"{i}-{j}\n")


data ={"virat":[100,200,230],"Rohit":[60,264,123],"rahul":[100,90,87]}    
#virat.txt --> score --> total
# match1 = 100
# total = 530