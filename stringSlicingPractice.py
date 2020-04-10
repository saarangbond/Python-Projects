def stringReplace(str, replaceChar, ind):
    str1 = str[0:ind] + replaceChar + str[ind+1:len(str)]
    str = str1
    return str1
    
if __name__ == "__main__":
    print()
    str = input("Input the string:: ")
    replaceChar = input("Input the replaceChar:: ")
    ind = input("Input the index:: ")
    print(stringReplace(str, replaceChar, int(ind)))