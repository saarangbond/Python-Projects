import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
purchases = pd.DataFrame(data, index = ["Jack", "Jill", "Robert", "Lily"])

print(purchases)

print(purchases.loc["Robert"])


purchases.to_csv("new_purchases.csv")
print()

orders = pd.read_csv('orders.csv')
print(orders)

# can use pd.read_json('filename.json') to read json files