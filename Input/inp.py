def add():
    x = input("Input the first number:: ")
    y = input("Input the second number:: ")

    result = int(x) + int(y)
    print(result)
    
##Use this to execute a specific function only when
##running this specific file
##Useful when this file is used as a module elsewhere
if __name__ == "__main__":
    add()