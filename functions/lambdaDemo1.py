x = lambda : print("lambda called...")
x()

add = lambda a,b : print(f"add = {a+b}")
add(10,20)

avg = lambda a,b,c : (a + b + c) /3
print(avg(10,20,30))

#if

findMax = lambda a, b:a if a>b else b
print(findMax(100,9))

findMax2 = lambda a ,b, c :a if a>b and a>c else (b if b>c else c)
print(findMax2(1,2,4))



def checkPalindrome(name):
    return name == name[::-1]

isPalindrome = lambda x: checkPalindrome(x)
print(isPalindrome("amit"))
