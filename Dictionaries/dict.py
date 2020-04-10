account = {"bank_name":"CCU", "balance":100, "address":"Dreamland APT"}
print(len(account))
print(account.keys())
print(account.values())
print(account.items())

print()

for k,v in account.items() :
    print(k,v)
    
##dictionaries only take unique keys. A dictionary will take the latest value for a key

print()

print(account['balance'])
print(account['address'])
##this way of accessing key-value pairs can cause an
##exception if a key is not present in the dictionary
##the .get() method is a safer way of accessing key-value pairs
print()

print(account.get("pin"))
print(account.get("bank_name"))

print()

account["AptNum"] = 301
print(account)

account.update({"bank_name":"DCU", "city":"SFO", "country":"USA"})
print(account)

print()

##the .get method accepts another parameter
##as the default return value
print(account.get("State", "Not present"))
print(account.get("bank_name", "Not present"))