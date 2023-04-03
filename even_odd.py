def evenodd_check(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = 5
res = evenodd_check(x)
if res == True:
    print("x is even")
else:
    print("x is odd")
