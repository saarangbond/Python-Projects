
def finalEx(arg1, arg2, *args, **kwargs):
    print("the first arg is " + arg1)
    print("the second arg is " + arg2)
    
    for items in args:
        print("element of args: ", items)
        
    for k, v, in kwargs.items():
        print (k + "----" + v)
        
finalEx("math", "science", "geography", "physics", calculus = "marov", physical = "irodov")