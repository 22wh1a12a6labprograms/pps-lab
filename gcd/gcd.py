def GCD(x,y):
    while(y):
        x,y=y,x%y
    return abs(x)
print("the GCD of 10 and 30 is : ","end=")
print(GCD(10,30))
