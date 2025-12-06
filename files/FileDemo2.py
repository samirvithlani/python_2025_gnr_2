# file = open("th.txt","r")
# data = file.read()
# print(data)

# file = open("th.txt","r")

# for i in file:
#     print(i,end="")

# file = open("th.txt","r")
# x = file.readline()
# print(x)

# file = open("th.txt","r")
# while True:
#     data = file.readline()
#     print(data,end="")
#     if not data:
#         break

file = open("th.txt","r")
# x = file.readlines()
# print(x)
for i in file.readlines():
    print(i,end="")